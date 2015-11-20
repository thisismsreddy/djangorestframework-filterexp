from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from quickstart import views


urlpatterns = [
    url(r'^friends/$', views.MyView.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)