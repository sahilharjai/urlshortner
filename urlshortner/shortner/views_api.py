from rest_framework import generics,mixins
from .models import URL,AnalyseUrl
from .serializers import URLCreateSerializer
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .extractor import get_features
from .final_prediction import pred
import math 
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
import time 

class URLCreateView(generics.CreateAPIView):
	authentication_classes = []
	serializer_class = URLCreateSerializer
	queryset = URL.objects.all()

	def create(self,request):
		url = request.data['url']
		if not "http" in url:
			url = "http://" + url
		url_count = URL.objects.filter(url=url).count()
		if url_count != 0:
			time.sleep(3)
			url_obj = URL.objects.filter(url=url)[0]
			print("hello")
			analyse_obj = get_object_or_404(AnalyseUrl,shortcode=url_obj)

		else:
			url_obj = URL.objects.create(url=url)
			url_obj.save()
			context = get_features(url_obj.url)
			dubl = []
			for i in range(0,14):
				dubl.append(context[i])
			value = pred(dubl)
			if value[0][0]>=0.50:
				result=1
			else:
				result=0
			analyse_obj = AnalyseUrl.objects.create(
					shortcode=url_obj,
					result=result,
					reliable_ip=context[0],
					length_of_url=context[1],
					shortened_url=context[2],
					contains_at_the_rate=context[3],
					cotains_double_slash=context[4],
					contains_hyphen=context[5],
					https_token=context[10],
					has_https=context[7],
					subdomain_length=context[6],
					ports=context[9],
					age_of_domain=context[11],
					dns_record=context[8],
					existing_dns_record=context[12],
					site_popularity=context[13],
					a_tag=context[14],
					form_tag=context[15],
					using_mail=context[16],
					abnormal_url=context[17],
					google_index=context[18]
				)
			analyse_obj.save()

		result_dict ={
			'result':analyse_obj.result,
			'longUrl':url_obj.url,
			'shortCode':url_obj.shortcode,
			'site_popularity':analyse_obj.site_popularity,
			'length_of_url':analyse_obj.length_of_url,
			'existing_dns_record':analyse_obj.existing_dns_record,
			'age_of_domain':analyse_obj.age_of_domain,
			'ports':analyse_obj.ports,
			'reliable_ip':analyse_obj.reliable_ip,
			'shortened_url':analyse_obj.shortened_url,
			'contains_at_the_rate':analyse_obj.contains_at_the_rate,
			'cotains_double_slash':analyse_obj.cotains_double_slash,
			'contains_hyphen':analyse_obj.contains_hyphen,
			'https_token':analyse_obj.https_token,
			'subdomain_length':analyse_obj.subdomain_length,
			'has_https':analyse_obj.has_https,
			'dns_record':analyse_obj.dns_record,
			'a_tag':analyse_obj.a_tag,
			'form_tag':analyse_obj.form_tag,
			'using_mail':analyse_obj.using_mail,
			'abnormal_url':analyse_obj.abnormal_url,
			'google_index':analyse_obj.google_index
		}
		return Response(result_dict)


class URLRedirectView(APIView):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = URL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        return HttpResponseRedirect(obj.url)


'''
	my_list=[is_ip,suspicious_url,shortened_url,contains_at_the_rate,contains_double_slash,
	contains_hyphen,check_subdomains,has_https,domain_reg_len,ports,https_token,
	age_domain,dns_record,popularity,a_tag,form_tag,using_mail,abnormalUrl,google_index]
'''