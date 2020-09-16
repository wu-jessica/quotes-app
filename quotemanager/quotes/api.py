from quotes.models import Quote
from rest_framework import viewsets, permissions
from .serializers import QuoteSerializer

# Quote Viewset
class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = QuoteSerializer