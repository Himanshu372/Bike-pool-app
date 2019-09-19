from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url

# router = routers.DefaultRouter()
# # router.register(r'', views.home)
# router.register(r'find_ride', views.searchRide)
# router.register(r'offer_ride', views.offerRide())



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.home),
    url(r'^offer_ride', views.offerRide, name = 'offer_ride'),
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]