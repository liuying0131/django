from django.conf.urls import patterns, include, url

from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite5.views.home', name='home'),

      url(r'^admin/', include(admin.site.urls)),
        url(r'^$', 'form_app.views.login',name='login'),
        url(r'^login/$', 'form_app.views.login',name='login'),
        url(r'^regist/$', 'form_app.views.regist',name='regist'),
        url(r'^index/$', 'form_app.views.index',name='index'),
        url(r'^logout/$', 'form_app.views.logout',name='logout'),
        url(r'^share/$', 'form_app.views.share',name='share'),
        url(r'^index/addstudent/$', 'form_app.views.addstudent',name='addstudent'),
        url(r'^index/addgrade/$', 'form_app.views.addgrade',name='addgrade'),
        url(r'^index/searchgrade/$', 'form_app.views.searchgrade',name='searchgrade'),
        url(r'^index/viewstudent/$', 'form_app.views.viewstudent',name='viewstudent'),
        url(r'^index/viewclass/$', 'form_app.views.viewclass',name='viewclass'),
        url(r'^index/viewclassstu/$', 'form_app.views.viewclassstu',name='viewclassstu'),
        url(r'^index/changepsw/$', 'form_app.views.changepsw',name='changepsw'),
        url(r'^index/editstudent/$', 'form_app.views.editstudent',name='editstudent'),
        url(r'^index/editgrade/$', 'form_app.views.editgrade',name='editgrade'),
        url(r'^index/altergrade/$', 'form_app.views.altergrade',name='altergrade'),
        url(r'^index/viewreview/$', 'form_app.views.viewreview',name='viewreview'),
        url(r'^index/review/$', 'form_app.views.review',name='review')
)