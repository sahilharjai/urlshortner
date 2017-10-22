from extractor import *
import csv
def new_write():
	f2=open('new_data.csv', 'w')
	fieldnames = ['has_ip', 'long_url','short_service','has_at',
		'double_slash_redirect','pref_suf','has_sub_domain','ssl_state',
		'long_domain','port','https_token','domain_Age','dns_record',
		'traffic','Result']
	writer = csv.DictWriter(f2, fieldnames=fieldnames)
	writer.writeheader()


	filename=open('data.txt','r')
	k=filename.readlines()
	for each in k:
		results=each.split(',')
		url=results[0]
		output=results[1].split('\n')[0]
		my_list=get_features(str(url))
		my_list.append(output)

		writer.writerow({'has_ip': str(my_list[0]), 'long_url': str(my_list[1]),
		'short_service':str(my_list[2]),'has_at':str(my_list[3]),'double_slash_redirect':str(my_list[4]),
			'pref_suf':str(my_list[5]),'has_sub_domain':str(my_list[6]),'ssl_state':str(my_list[7]),
			'long_domain':str(my_list[8]),'port':str(my_list[9]),'https_token':str(my_list[10]),
			'domain_Age':str(my_list[11]),'dns_record':str(my_list[12]),'traffic':str(my_list[13]),
			'Result':str(my_list[14])}
			)




new_write()

'''
has_ip,long_url,short_service,has_at,double_slash_redirect,pref_suf,
has_sub_domain,ssl_state,long_domain,port,https_token,
domain_Age,dns_record,traffic,Result
'''