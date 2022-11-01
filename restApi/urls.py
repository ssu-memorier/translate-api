from django.conf.urls import url

from . import views

urlpatterns = [
    # ^:starts with , $:ends with
    url(r'^translate$', views.googleTranslate),
]
