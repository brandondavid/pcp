TEMPLATE	= app
LANGUAGE	= C++
HEADERS		= pmchart.h main.h \
		  aboutdialog.h chartdialog.h exportdialog.h \
		  hostdialog.h infodialog.h openviewdialog.h \
		  recorddialog.h samplesdialog.h saveviewdialog.h \
		  searchdialog.h seealsodialog.h settingsdialog.h \
		  tab.h tabdialog.h \
		  chart.h colorbutton.h colorscheme.h statusbar.h \
		  namespace.h \
		  tabwidget.h timeaxis.h timecontrol.h \
		  groupcontrol.h gadget.h sampling.h tracing.h \
                  metricdetails.h
SOURCES		= pmchart.cpp main.cpp \
		  aboutdialog.cpp chartdialog.cpp exportdialog.cpp \
		  hostdialog.cpp infodialog.cpp openviewdialog.cpp \
		  recorddialog.cpp samplesdialog.cpp saveviewdialog.cpp \
		  searchdialog.cpp seealsodialog.cpp settingsdialog.cpp \
		  tab.cpp tabdialog.cpp \
		  chart.cpp colorbutton.cpp colorscheme.cpp statusbar.cpp \
		  namespace.cpp \
		  tabwidget.cpp timeaxis.cpp timecontrol.cpp \
		  groupcontrol.cpp gadget.cpp sampling.cpp tracing.cpp \
		  view.cpp metricdetails.cpp
FORMS		= aboutdialog.ui chartdialog.ui exportdialog.ui \
		  hostdialog.ui infodialog.ui pmchart.ui openviewdialog.ui \
		  recorddialog.ui samplesdialog.ui saveviewdialog.ui \
		  searchdialog.ui seealsodialog.ui settingsdialog.ui \
		  tabdialog.ui metricdetails.ui
ICON		= pmchart.icns
RC_FILE		= pmchart.rc
RESOURCES	= pmchart.qrc
INCLUDEPATH	+= ../include
INCLUDEPATH	+= ../libpcp_qed/src ../libpcp_qmc/src ../libpcp_qwt/src
CONFIG		+= qt warn_on
CONFIG(release, release|debug) {
DESTDIR	= build/release
}
CONFIG(debug, release|debug) {
DESTDIR	= build/debug
}
LIBS		+= -L../libpcp/src
LIBS		+= -L../libpcp_qed/src -L../libpcp_qed/src/$$DESTDIR
LIBS		+= -L../libpcp_qmc/src -L../libpcp_qmc/src/$$DESTDIR
LIBS		+= -L../libpcp_qwt/src -L../libpcp_qwt/src/$$DESTDIR
LIBS		+= -lpcp_qed -lpcp_qmc -lpcp_qwt -lpcp
win32:LIBS	+= -lwsock32 -liphlpapi
QT		+= printsupport network svg widgets
QMAKE_INFO_PLIST = pmchart.info
QMAKE_CFLAGS	+= $$(CFLAGS)
QMAKE_CXXFLAGS	+= $$(CFLAGS) $$(CXXFLAGS)
QMAKE_LFLAGS	+= $$(LDFLAGS)
