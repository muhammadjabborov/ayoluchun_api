from django.urls import path

from apps.common.views import CreateRegionAPIVIew, ListRegionAPIView, RetrieveRegionAPIView, UpdateRegionAPIView, \
    DeleteRegionAPIView, CreateCountryAPIVIew, ListCountryAPIView, RetrieveCountryAPIView, UpdateCountryAPIView, \
    DeleteCountryAPIView

urlpatterns = [
    path('common/create/country/', CreateCountryAPIVIew.as_view()),
    path('common/list/country/', ListCountryAPIView.as_view()),
    path('common/retrieve/country/<int:pk>/', RetrieveCountryAPIView.as_view()),
    path('common/update/country/<int:pk>/', UpdateCountryAPIView.as_view()),
    path('common/delete/country/<int:pk>/', DeleteCountryAPIView.as_view()),
    path('common/create/region/', CreateRegionAPIVIew.as_view()),
    path('common/list/region/', ListRegionAPIView.as_view()),
    path('common/retrieve/region/<int:pk>/', RetrieveRegionAPIView.as_view()),
    path('common/update/region/<int:pk>/', UpdateRegionAPIView.as_view()),
    path('common/delete/region/<int:pk>/', DeleteRegionAPIView.as_view()),
]
