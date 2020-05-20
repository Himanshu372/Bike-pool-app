from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
#
# router = routers.DefaultRouter()
# # # router.register(r'', views.home)
# router.register(r'find_ride', views.FindRide)
# router.register(r'offer_ride/(?P<.*>)', views.OfferRide)
# router.register(r'login', views.UserLogin)
# router.register(r'signup', views.UserSignup)






# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.home, name='home'),
    # path('', include(router.urls)),
    url(r'find_ride', views.FindRide.as_view({'get': 'list', 'post': 'create'}), name='find_ride'),
    url(r'^offer_ride', views.OfferRide.as_view({'get': 'list', 'post': 'create'}), name='offer_ride'),
    url(r'^login', views.UserLogin.as_view({'get': 'list', 'post': 'create'}), name='login'),
    url(r'^signup', views.UserSignup.as_view({'get': 'list', 'post': 'create'}), name='signup'),
    url(r'^show_rides', views.ShowRides.as_view({'get': 'list', 'post': 'create'}), name='show_rides'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['html', 'json'])