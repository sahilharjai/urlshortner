from rest_framework import generics,mixins
from .models import URL
from .serializers import URLCreateSerializer
from rest_framework.views import APIView
from rest_framework import permissions


class URLCreateView(generics.CreateAPIView):
	authentication_classes = []
	serializer_class = URLCreateSerializer
	queryset = URL.objects.all()

	def create(self,request):
		url_serializer = URLCreateSerializer(data=request.data)
		if url_serializer.is_valid():
			url = url_serializer.save()
			return Response(url_serializer.data)
		return Response(url_serializer.errors)