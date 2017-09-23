from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.Helloviewsets, base_name='hello-viewset')
router.register('profile', views.UserProfileViewset)

urlpatterns = [
     url(r'^hello-view/', views.Helloapiview.as_view()),
     url(r'', include(router.urls))
]
