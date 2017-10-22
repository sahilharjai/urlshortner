from rest_framework import generics,mixins
from .models import URL
from .serializers import URLCreateSerializer
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .extractor import get_features
from .final_prediction import pred
import math 
from django.http import HttpResponse, HttpResponseRedirect, Http404
class URLCreateView(generics.CreateAPIView):
	authentication_classes = []
	serializer_class = URLCreateSerializer
	queryset = URL.objects.all()

	def create(self,request):

		print("serializer",request.data)
		print("serializer",request.data['url'])
		url = request.data['url']
		if not "http" in url:
			url = "http://" + url
		url_count = URL.objects.filter(url=url).count()
		if url_count != 0:
			url_obj = URL.objects.filter(url=url)[0]
			print("obj",url_obj)
		else:
			url_obj = URL.objects.create(url=url)
			url_obj.save()
		print("url before",url_obj.url)
		context = get_features(url_obj.url)
		print("hhhhhahahaha",context)
		value = pred(context)
		print("value",value)
		if value[0][0]>=0.50:
			result=1
		else:
			result=0
		result_dict ={
			'result':result,
			'longUrl':url_obj.url,
			'shortCode':url_obj.shortcode,
			'site_popularity':context[13],
			'length_of_url':context[1],
			'existing_dns_record':context[12],
			'age_of_domain':context[11],
			'ports':context[9]
		}
		return Response(result_dict)


class URLRedirectView(APIView):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = URL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        return HttpResponseRedirect(obj.url)