#! /usr/bin/python

import requests, argparse, subprocess, os

parser = argparse.ArgumentParser(description='qa/660.py pmwebapi check')
parser.add_argument('--version', action='version', version='1')
parser.add_argument('--host', required=True)
parser.add_argument('--port', default=44323)
args = parser.parse_args()

url = 'http://' + args.host + ':' + str(args.port) + '/'
devnull = os.open(os.devnull, os.O_RDWR)
os.unsetenv('http_proxy')
os.unsetenv('HTTP_PROXY')

# ------------------------------------------------------------------------

# test - create contexts
req = requests.get(url=url + 'pmapi/context?local=foo')
resp = req.json()
ctx_local = resp['context']
print 'Received PM_CONTEXT_LOCAL #'+str(ctx_local)

req = requests.get(url=url + 'pmapi/context?hostname=' + args.host)
resp = req.json()
ctx_host = resp['context']
print 'Received PM_CONTEXT_HOST #'+str(ctx_host)

# ------------------------------------------------------------------------

# all these should get an error
req = requests.get(url=url + 'pmapi/context?archivefile=/dev/null')
print 'bad archive /dev/null response code ' + str(req.status_code) 

req = requests.get(url=url + 'pmapi/context?archivefile=../../etc/passwd')
print 'bad archive ../../etc/passwd response code ' + str(req.status_code) 

req = requests.get(url=url + 'pmapi/NOSUCHAPI')
print 'command NOSUCHAPI response code ' + str(req.status_code) 

req = requests.get(url=url + 'pmapi/NOSUCHCONTEXT/_metric')
print 'context NOSUCHCONTEXT response code ' + str(req.status_code) 

req = requests.get(url=url + 'pmapi/0/_metric')
print 'context 0 response code ' + str(req.status_code) 

req = requests.get(url=url + 'random_nonpmwebapi_url')
print 'non-pmwebapi response code ' + str(req.status_code) 

# ------------------------------------------------------------------------

def test_metric_enumeration(ctx, prefix):
    ctxurl = url + 'pmapi/' + str(ctx) + '/'
    if (ctx == ctx_local):
        procargs = ['pminfo', '-L']
    else:
        procargs = ['pminfo', '-h', args.host]
    if (prefix != ''):
        procargs.append(prefix)
    proc = subprocess.Popen(procargs,
                            stdout=subprocess.PIPE, 
                            stderr=devnull)
    num_metrics = 0
    while True:
        line = proc.stdout.readline()
        if line != '':
            num_metrics = num_metrics + 1
        else:
            break

    testprefix='test #'+str(ctx)+' metric '+prefix+'.*'
    print testprefix+ ' enumeration with pminfo #'+str(num_metrics)

    req = requests.get(url=ctxurl + '_metric' + \
                           ('?prefix='+prefix if prefix != '' else ''))
    resp = req.json()
    print testprefix + ' enumeration with pmwebinfo #'+str(len(resp['metrics']))
    if (abs(len(resp['metrics']) - num_metrics) < 10): # allow some variation
        print testprefix + ' enumeration match count PASS'
    else:
        print testprefix + ' enumeration match count FAIL'


test_metric_enumeration(ctx_local,'')
test_metric_enumeration(ctx_host,'')
test_metric_enumeration(ctx_local,'kernel')
test_metric_enumeration(ctx_host,'kernel')

# ------------------------------------------------------------------------

# empty _fetch should get an error
req = requests.get(url=url + 'pmapi/'+str(ctx_host)+'/_fetch')
print 'context #'+str(ctx_host)+' response code ' + str(req.status_code) 

# ------------------------------------------------------------------------

