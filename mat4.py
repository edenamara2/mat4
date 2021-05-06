import requests
f1=open('dests.txt','r',encoding='utf-8')
key='_____________________'
adress='תל אביב'
rsp1=dict()
rsp2=dict()
data=dict()
distance=dict()

for line in f1:
    url_g="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (line.strip(),key) 
    url_d="https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&key=%s&destinations=%s" % (adress,key,line.strip())
    rsp1[line.strip()] = requests.get(url_g).json()
    rsp2[line.strip()] = requests.get(url_d).json()
    data[line.strip()] = (rsp1[line.strip()]['results'][0]['geometry']['location']['lng'],rsp1[line.strip()]['results'][0]['geometry']['location']['lat'],rsp2[line.strip()]['rows'][0]['elements'][0]['distance']['text'], rsp2[line.strip()]['rows'][0]['elements'][0]['duration']['text'])
    print("county:" + str(line.strip()))
    print('The distance is: '+ str(data[line.strip()][2]))
    print('The time is: '+ str(data[line.strip()][3]))
    print('The lag is:'+ str(data[line.strip()][0]))
    print('The lat is: '+ str(data[line.strip()][1]))
    print('___________________________________________________')
    distance[line.strip()]= (rsp2[line.strip()]['rows'][0]['elements'][0]['distance']['value'])

from operator import itemgetter
distancevalue=(sorted(distance.items(),key= itemgetter(1),reverse=True))
print("the 3 biggest distance countrys are: ",distancevalue[0],distancevalue[1],distancevalue[2] )