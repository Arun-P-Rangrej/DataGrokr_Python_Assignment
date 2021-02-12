import urllib.request
import sys
import re
def antihtml(url):
	urllib.request.urlretrieve(sys.argv[1],'web')
	f=open('web').read()
	x=re.findall(r'>[^<]+<',f)
	for i in x:
		print(i[1:-1])
antihtml(sys.argv[1])
