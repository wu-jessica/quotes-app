from rest_framework import serializers
from quotes.models import Quote

# Quote Serializer
class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'