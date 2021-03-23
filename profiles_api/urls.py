from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset' )
#no need to specify the base_name in the one below because we have a queryset objects
#base_name is needed if a viewset does not have a queryset or you want to change the query set name.
router.register('profile', views.UserProfileViewSet)
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))

]
