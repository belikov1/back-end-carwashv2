from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from reviews.models import ReviewsModel
from reviews.serializers import ReviewsSerializers
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from djoser.urls.base import

class ReviewsView(APIView):

    def get(self, request):
        reviews = ReviewsModel.objects.order_by('date').reverse()
        serializers = ReviewsSerializers(reviews, many=True)
        return Response(serializers.data)

    def post(self, request):
        reviews = ReviewsSerializers(data=request.data)
        if reviews.is_valid():
            reviews.save()
            return Response({'status': 'add'})
        else:
            return Response({'status': "error"})


# @csrf_exempt
def index(request):
    return render(request, 'index.html')
