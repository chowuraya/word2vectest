import urllib.request
import json

url = 'http://155.238.46.32:30020/get/article'


body = {'linkUrl':'https://elections.thesouthafrican.com/political-parties/african-christian-democratic-party-acdp/'}



jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
#req.add_header('Content-Length', len(jsondataasbytes))
#print (jsondataasbytes)
#response = urllib.request.urlopen(req, jsondataasbytes)

data = urllib.parse.urlencode(body)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
req.add_header('Content-Type', 'application/json; charset=utf-8')
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print(the_page)