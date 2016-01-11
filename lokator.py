#!/usr/bin/python

import pygeoip
import requests
print "\n****************************************************"
print "*                                          	   *"
print "*| |         | |       | |                         *"
print "*| |     ___ | | ____ _| |_ ___  _ __ _ __  _   _  *"
print "*| |    / _ \| |/ / _` | __/ _ \| '__| '_ \| | | | *"
print "*| |___| (_) |   < (_| | || (_) | |_ | |_) | |_| | *"
print "*\_____/\___/|_|\_\__,_|\__\___/|_(_)| .__/ \__, | *"
print "*		                                | |    __/  | *"
print "*		                                |_|   |___ /  *"
print "*Lokator.py                                        *"
print "****************************************************\n\n"

str = raw_input('Enter the IP address you wish to geolocate: ')
r = requests.get('http://ipinfo.io/ ' + str)
rp = pygeoip.GeoIP('/usr/share/GeoIP/GeoIPCity.dat')
rg = requests.get('http://www.geoplugin.net/json.gp?ip= ' + str)
rb = requests.get('http://getcitydetails.geobytes.com/GetCityDetails?fqcn= ' + str)




loc = r.json(), rp.record_by_addr(str), rg.text, rb.text
for x in loc:
	print x
