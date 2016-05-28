from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_all_posts, name='show_all_posts'),
]

# Create your views here.
