from rest_framework import routers

from api.views import ApplicationViewSet

router = routers.DefaultRouter()
router.register('products', ApplicationViewSet, base_name='core')

urlpatterns = router.urls