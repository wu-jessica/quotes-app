from rest_framework import routers
from .api import QuoteViewSet

router = routers.DefaultRouter()
router.register('api/quotes', QuoteViewSet, 'quotes')

urlpatterns = router.urls