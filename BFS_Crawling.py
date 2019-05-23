from bs4 import BeautifulSoup
import requests
import queue

count=0
q=queue.Queue(maxsize=50000)

f=open("url.txt","w")
f2=open("text.txt","w")

start = "www.pec.ac.in"
q.put(start)
while (q.qsize()>0):
	url=q.get()
	if count==0:	
		r  = requests.get("http://"+url)
		
	elif url.startswith("http://") or url.startswith("https://"):
		r=requests.get(url)
		
	elif url.startswith('/'):
		url2="http://"+start+url
		r  = requests.get(url2)
		
	else:
		continue
		
	print(url)
	data = r.text
	soup = BeautifulSoup(data,'lxml')

	for link in soup.find_all('a'):
		no1=link.get('href')
		no2=link.text

		if no1!=None:
			f.write(no1+'\n')
			f2.write(no2+'\n')
			q.put(no1)
			count+=1

print('-----Terminated sucessfully-----')