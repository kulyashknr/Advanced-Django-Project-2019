from rest_framework import routers

from api.views import VacancyViewSet

router = routers.DefaultRouter()
router.register('products', VacancyViewSet, base_name='core')

urlpatterns = router.urls