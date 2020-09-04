from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
keyword=input()
myurl='https://www.flipkart.com/search?q='+keyword+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
uclient=ureq(myurl)
pagehtml=uclient.read()
uclient.close()
pagesoup=soup(pagehtml,"html.parser")

containers=pagesoup.findAll("div",{"class":"_1UoZlX"})

filename="project.txt"
f=open(filename,"w")
header="product name , price \n"
f.write(header)

for container in containers:
    title=container.findAll("div",{"class":"_3wU53n"})
    name=title[0].text
    price=container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})
    amount=price[0].text
    print("\n product name : " + name)
    f.write("\n"+name+"\n")
    i=1
    while i<len(amount):
        f.write(amount[i])
        i=i+1
    print("\n")    
        
    


f.close()



