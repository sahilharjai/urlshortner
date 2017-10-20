import os
from tld import get_tld
import tldextract
import pythonwhois
from datetime import datetime
import urllib
from xml.dom import minidom

def get_ip_address(domain_name):
	command="host " + domain_name
	process=os.popen(command)
	results=str(process.read())
	marker=results.find("has address")+12
	return results[marker:].splitlines()[0]

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