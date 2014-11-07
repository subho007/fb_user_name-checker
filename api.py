import urllib2
import json
print "Enter the username"
y=str(raw_input())
x="http://graph.facebook.com/"
z=str(x+y)
url=urllib2.urlopen(z)
data=json.load(url)
if data["first_name"]==" ":
    print "username available"
else:
    print data["first_name"]+" "+"own this"


