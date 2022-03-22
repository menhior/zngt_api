from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import Listing
from .serializers import ListingSerializer

@api_view(['GET'])
def getData(request):
	listings = Listing.objects.all()
	serializer = ListingSerializer(listings, many=True)
	return Response(serializer.data)