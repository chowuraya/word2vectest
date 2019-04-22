import requests
import pandas as pd
import json
import csv


reader = pd.read_csv('NewsURLs.csv',usecols=["URL"],squeeze=True)
outputCsv=open('output.csv','a')
csvwriter=csv.writer(outputCsv)
#output=open('output.txt','a')

for row in reader.values:
    print(row)
    data = {'linkUrl': '%s'%row}
    r = requests.post('http://155.238.46.32:30020/get/article', json=data )

    jsondata=json.loads(r.content)

    title=str(jsondata['title'])
    arti=str(jsondata['article'])

    dat=title,'#',arti
    outputCsv.write(str(dat))

    outputCsv.write('\n')
    print(jsondata['title'],jsondata['article'])

    #output.write(str(jsondata))
    #output.write("\n,")

outputCsv.close()
#output.close()
    #print(r.content)

   # result=pd.DataFrame(r)

