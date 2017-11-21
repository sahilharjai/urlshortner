from .utils import *

def get_features(url):
	suspicious_url=check_suspicious(url)
	shortened_url=check_shortening_services(url)
	contains_at_the_rate=check_the_rate(url)
	contains_double_slash=pos_of_double_slash(url)
	domain_name=get_domain_name(url)
	is_ip=domain_name['is_ip']
	domain_name=domain_name['domain_name']
	contains_hyphen=pos_of_hyphen(domain_name)
	https_token=check_https_token(domain_name)
	check_subdomains=get_subdomains(url)
	ip_address=get_ip_address(domain_name)
	has_https=get_https(url)
	dns_results=get_domain_reg_len(domain_name)
	age_domain=dns_results['age']
	dns_record=dns_results['dns_record']
	domain_reg_len=dns_results['reg_len']
	ports=port_check(ip_address)
	popularity=sitepopularity(domain_name)
	parsewebsite=parse_website(url)
	a_tag=parsewebsite['a_tag']
	form_tag=parsewebsite['form_tag']
	using_mail=parsewebsite['using_mail']
	abnormalUrl=abnormal_url(domain_name)
	google_index=googleIndex(url)

	context={"suspicious_url":suspicious_url,"shortened_url":shortened_url,
	"contains_at_the_rate":contains_at_the_rate,"contains_double_slash":contains_double_slash,
	"contains_hyphen":contains_hyphen,"https_token":https_token,
	"check_subdomains":check_subdomains,"has_https":has_https,
	"age_domain":age_domain,"dns_record":dns_record,
	"domain_reg_len":domain_reg_len,"ports":ports,"popularity":popularity,'a_tag':a_tag,
	'form_tag':form_tag,'using_mail':using_mail,'abnormal_url':abnormalUrl,'google_index':google_index}

	my_list=[is_ip,suspicious_url,shortened_url,contains_at_the_rate,contains_double_slash,
	contains_hyphen,check_subdomains,has_https,domain_reg_len,ports,https_token,
	age_domain,dns_record,popularity,a_tag,form_tag,using_mail,abnormalUrl,google_index]

	#print(context)
	return my_list