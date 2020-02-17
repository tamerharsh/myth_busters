#Program's intention is to ping a particular hostname with its's decimal ip_address equvialent. [ping www.google.com  or https:://<decimal_equivalent_of_ip_address>].
#Author: Harsh Tamrakar

import os
import socket

#target hostname.
host_name = 'www.ifm.com'

try:
 host_ip = socket.gethostbyname(host_name)
    
 #TODO:GET IP USING NSLOOKUP COMMAND
 #ip='nslookup'+' '+str(host_name)
 #host_ip=os.system(host)ip)

#split ip using '.' as delimiter.
 ip_parts=host_ip.split('.')

#starting from zeroth index => 127.15.25.23 =. 
 ip_parts.reverse()

#convert string to int.
 results = [int(i) for i in ip_parts]
 ip_in_decimal=0
 index=0
 

#convert octal values to decimal.
 for i in (results):
     ip_in_decimal=ip_in_decimal+i*pow(2, index)
     index+=8

 print('[host name]:'+host_name+' \n[ip]:'+host_ip+'\n[eqvivalent ip]:'+str(ip_in_decimal)+'\n')

 print('****ping to https:://'+str(ip_in_decimal)+'******')

#making command for ping https:://ip_in_decimal.
 cmd='ping'+' '+str(ip_in_decimal)
 os.system(cmd)

except:
    print('[error]:incorrect host name')
