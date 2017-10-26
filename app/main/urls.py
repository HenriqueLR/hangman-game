from django.conf.urls import include, url, patterns

urlpatterns = patterns('main.views',

    url(r'^$','home',name='home'),
    url(r'^sort/$','sort',name='sort'),
    url(r'^assert_word/$', 'assert_word', name='assert_word'),
    url(r'^clear_sessions/$', 'clear_sessions', name='clear_sessions'),
)