from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .models import AnalyseUrl,URL
# Create your views here.

def setCrossRight(data):
    if data==-1:
      return '-check right' 
    return '-times cross'

def setCrossRightOpp(data): 
    if data==1:   
      return '-check rightOp'   
    return '-times crossOp'
  
  

class URLHomeView(View):
    def get(self, request):
        return render(request, 'index.html')




class URLAnalyseView(View):
	def get(self, request,shortcode=None): 	
		qs = URL.objects.filter(shortcode__iexact=shortcode)
		if qs.count() != 1 and not qs.exists():
			raise Http404
		obj = qs.first()
		analyse_obj = get_object_or_404(AnalyseUrl,shortcode=obj)
		print("analyse",analyse_obj)

		if analyse_obj.result==1:
			result='<span class="safe">Safe<span>'
		else:
			result='<span class="phishing">Phishing<span>'

		if analyse_obj.site_popularity==-1:
			site_popularity = 'High'
			site_popularity_class = 'HighOp'  
		elif analyse_obj.site_popularity==0:
			site_popularity = 'Medium'
			site_popularity_class = 'Medium' 
		else:
			site_popularity = 'Low'
			site_popularity_class = 'LowOp'

		if analyse_obj.length_of_url==1:
			length_of_url = 'High'
		elif analyse_obj.length_of_url==0:
			length_of_url = 'Medium'
		else:
			length_of_url = 'Low'


		if analyse_obj.a_tag==1:
			a_tag = 'High'
		elif analyse_obj.a_tag==0:
			a_tag = 'Medium'
		else:
			a_tag = 'Low'


		if analyse_obj.subdomain_length==1:
			subdomain_length = 'High'
		elif analyse_obj.subdomain_length==0:
			subdomain_length = 'Medium'
		else:
			subdomain_length = 'Low'





		result_dict ={
			'safe_site':analyse_obj.result,
			'result':result,
			'longUrl':obj.url,
			'shortCode':obj.shortcode,
			'site_popularity':site_popularity,
			'site_popularity_class':site_popularity_class,
			'length_of_url':length_of_url,
			'a_tag':a_tag,
			'existing_dns_record':setCrossRight(analyse_obj.existing_dns_record),
			'age_of_domain':setCrossRight(analyse_obj.age_of_domain),
			'ports':setCrossRight(analyse_obj.ports),

			'reliable_ip':setCrossRight(analyse_obj.reliable_ip),
			'shortened_url':setCrossRight(analyse_obj.shortened_url),
			'contains_at_the_rate':setCrossRightOpp(analyse_obj.contains_at_the_rate),
			'cotains_double_slash':setCrossRightOpp(analyse_obj.cotains_double_slash),
			'contains_hyphen':setCrossRightOpp(analyse_obj.contains_hyphen),
			'https_token':setCrossRight(analyse_obj.https_token),
			'subdomain_length':subdomain_length,
			'has_https':setCrossRight(analyse_obj.has_https),
			'dns_record':setCrossRight(analyse_obj.dns_record),
			'form_tag':setCrossRightOpp(analyse_obj.form_tag),
			'abnormal_url':setCrossRightOpp(analyse_obj.abnormal_url),
			'using_mail':setCrossRightOpp(analyse_obj.using_mail),
			'google_index':setCrossRight(analyse_obj.google_index)
		}
		print(result_dict)

		return render(request, 'analyse.html',result_dict)