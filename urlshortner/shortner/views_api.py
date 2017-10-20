from rest_framework import generics,mixins
from .models import URL
from .serializers import URLCreateSerializer
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .extractor import get_features
from .final_prediction import pred

class URLCreateView(generics.CreateAPIView):
	authentication_classes = []
	serializer_class = URLCreateSerializer
	queryset = URL.objects.all()

	def create(self,request):
		url_serializer = URLCreateSerializer(data=request.data)
		if url_serializer.is_valid():
			url = url_serializer.save()
			context = []
			print("aaaaaa",url.url)
			context = get_features(url.url)
			print("hhhhhahahaha",context)
			pred(context)
			return Response('www.google.co.in')
		return Response(url_serializer.errors)