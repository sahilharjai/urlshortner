import os
from tld import get_tld
import tldextract
import pythonwhois
from datetime import datetime
import urllib
from xml.dom import minidom
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from urllib.parse import urlparse

def get_ip_address(domain_name):
	try:
		command="host " + domain_name
		process=os.popen(command)
		results=str(process.read())
		marker=results.find("has address")+12
		return results[marker:].splitlines()[0]
	except:
		return None

def check_suspicious(url):
	if(len(url)<54):
		return -1
	if(len(url)>=54 and len(url)<=75):
		return 0
	return 1


def check_shortening_services(url):
	string=str(url)
	if(string.find("bit.ly")!=-1):
		return 1
	if(string.find("goo.gl")!=-1):
		return 1
	return -1

def check_the_rate(url):
	string=str(url)
	if (string.find('@')!=-1):
		return 1
	return -1

def pos_of_double_slash(url):
	string=str(url)
	cmp_str=string[:8]
	cmp_str=cmp_str.lower()
	if(cmp_str=="https://"):
		string=string[8:]
	else:
		string=string[7:]
	if(string.find("//")!=-1):
		return 1
	else:
		return -1

def get_domain_name(url):
	try:
		domain_name=get_tld(url)
		k={}
		k['domain_name']=domain_name
		k['is_ip']=-1
		return k
	except:
		k={}
		k['is_ip']=1
		k['domain_name']=url
		return k


def pos_of_hyphen(domain_name):
	name=str(domain_name)
	if(name.find('-')!=-1):
		return 1
	return -1

def check_https_token(domain_name):
	name=str(domain_name)
	if(name.find('https')!=-1):
		return 1
	return -1


def get_subdomains(url):
	results=tldextract.extract(url)
	subdomains=list(results[0].split('.'))
	length=len(subdomains)
	if 'www' in subdomains:
		length=length-1
	if '' in subdomains:
		length=length-1
	if length==1:
		return 0
	if length>1:
		return 1
	return -1


def get_https(url):
	string=str(url)
	cmp_str=string[:8]
	cmp_str=cmp_str.lower()
	if(cmp_str=="https://"):
		return -1
	return 1

def get_domain_reg_len(domain_name):
	try:
		results=pythonwhois.get_whois(domain_name)
		start_date=results['creation_date']
		end_date=results['expiration_date']

		diff=abs((end_date[0]-start_date[0]).days)
		context={}
		if(diff>365):
			context['reg_len']=-1
		else:
			context['reg_len']=1
		if(diff>=183):
			context['age']=-1
		else:
			context['age']=1
		context['dns_record']=-1
		return context
	except:
		context={}
		context['age']=1
		context['dns_record']=1
		context['reg_len']=1
		return context


def port_check(ip_address):
	try:
		options="-F"
		command="nmap "+options+" "+ip_address
		process=os.popen(command)
		results=str(process.read())
		results=results.lower()
		if (results.find('ftp')!=-1):
			return 1
		if (results.find('ssh')!=-1):
			return 1
		if(results.find('remote desktop')!=-1):
			return 1
		if(results.find('telnet')!=-1):
			return 1
		if(results.find('smb')!=-1):
			return 1
		if(results.find('mssql')!=-1):
			return 1
		if(results.find('oracle')!=-1):
			return 1
		if(results.find('mysql')!=-1):
			return 1
		return -1
	except:
		return 1


def find_ele_with_attribute(dom,ele,attribute):
    for subelement in dom.getElementsByTagName(ele):
        if subelement.hasAttribute(attribute):
            return subelement.attributes[attribute].value
    return None
def sitepopularity(domain_name):
	try:
		xmlpath='http://data.alexa.com/data?cli=10&dat=snbamz&url='+domain_name
		xml= urllib.request.urlopen(xmlpath)
		dom =minidom.parse(xml)
		rank_host=find_ele_with_attribute(dom,'POPULARITY','TEXT')
		if rank_host==None:
			return 1
		rank_host=int(rank_host)
		if rank_host<=100000:
			return -1
		else:
			return 0
	except:
		return 1

def abnormal_url(domain_name):
	try:
		k=pythonwhois.get_whois(domain_name)
		return -1
	except:
		return 1


def googleIndex(url):
	try:
		url = urlparse(url)
		host_name=url.hostname
	except:
		return 1
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
	headers = { 'User-Agent' : user_agent}
	query = {'q': 'info:' + host_name}
	proxies = {
    'https' : 'https://localhost:8123',
    'https' : 'http://localhost:8123'
    }
	try:
		google = "https://www.google.com/search?" + urlencode(query)
		data = requests.get(google, headers=headers)
		data.encoding = 'ISO-8859-1'
		soup = BeautifulSoup(str(data.content), "html.parser")
	except:
		return 1
	try:
		check = soup.find(id="rso").find("div").find("div").find("h3").find("a")
		href = check['href']
		return -1
	except AttributeError:
		return 1


def parse_website(url):
	try:
		r=requests.get(url)
		soup=BeautifulSoup(r.text)
	except:
		return {'a_tag':-1,'form_tag':1,'using_mail':1}
	try:
		k=soup.find_all('a')
		count_a=len(k)
		leg_a_count=0
		for each in k:
			if each['href'].startswith('#'):
				leg_a_count=leg_a_count+1
			elif each['href'].startswith('/'):
				leg_a_count=leg_a_count+1
			elif each['href'].startswith("JavaSript"):
				leg_a_count=leg_a_count+1
			elif each['href'].startswith(host_name):
				leg_a_count=leg_a_count+1
		a_tag=-1
		if count_a==0:
			a_tag=-1
		p=(float(leg_a_count)/float(count_a))*100
		if p<31:
			a_tag=-1
		if p>=31 and p<=67:
			a_tag=0
		if p>67:
			a_tag=1
	except:
		a_tag=-1
	try:
		form_tags=soup.find_all('form')
		count_form_tags=len(form_tags)
		form_tag=-1
		for each in form_tags:
			if not each['action'] or each['action']=='':
				form_tag=1
				break
	except:
		form_tag=-1
	try:
		using_mail=-1
		k=soup.find_all('a')
		for each in k:
			if each['href'] and each['href'].startswith('mailto'):
				using_mail=1
				break
	except:
		using_mail=-1
	context={'a_tag':a_tag,'form_tag':form_tag,'using_mail':using_mail}
	return context
