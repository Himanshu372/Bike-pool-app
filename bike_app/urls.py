from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url

router = routers.DefaultRouter()
# # router.register(r'', views.home)
router.register(r'find_ride', views.FindRide)
router.register(r'offer_ride', views.OfferRide)
router.register(r'login', views.UserLogin)
router.register(r'signup', views.UserSignup)






# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.home),
    # url(r'^offer_ride', views.offerRide, name = 'offer_ride'),
    # url(r'^find_ride', views.findRide, name = 'find_ride'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

