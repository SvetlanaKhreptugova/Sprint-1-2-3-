from rest_framework import routers
from .views import Passviewset
from django.urls import path, include
from .yasg import urlpatterns as doc_url

router = routers.DefaultRouter()
router.register(r'submitData', Passviewset, basename='submitData')

urlpatterns = [
    path('', include(router.urls)),

]

urlpatterns += doc_url
