from django.urls import path, include

urlpatterns = [
    path('', include('apps.account.urls')),
    path('', include('apps.blog.urls')),
    # path('', include('apps.course.urls')),
    # path('', include('apps.other.urls')),
    # path('', include('apps.payment.urls'))
]
