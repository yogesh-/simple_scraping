import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.yellowpages.com/search?search_terms=coffe&geo_location_terms=Los+Angeles%2C+CA"
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")
#for link in links:
	#print "<a href='%s'>%s</a>"%(link.get("href"),link.text)

g_data = soup.find_all("div",{"class":"info"})

list_info = []

for item in g_data:
	business_name=item.contents[0].find_all("a",{"class":"business-name"})[0].text
	try:
		streetAddress = item.contents[1].find_all("a",{"itemprop":"streetAddress"})[0].text
	except:
		pass
	try:
		addressLocality = item.contents[1].find_all("span", {"itemprop":"addressLocality"})[0].text.replace(',','')
	except:
		pass
	try:
		addressRegion = item.contents[1].find_all("span", {"itemprop":"addressRegion"})[0].text
	except: 
		pass
	try:
		postalCode = item.contents[1].find_all("span", {"itemprop":"postalCode"})[0].text
	except: 
		pass
	# try:
	# 	print item.contents[1].find_all("li", {"class":"primary"})[0].text
	# except:
	# 	pass
	y = business_name,addressRegion,addressLocality,postalCode
list_info.append(y)
print list_info
resultFile = open("output.csv",'wb')
writer = csv.writer(resultFile)
for item in list_info:
	writer.writerow([item])


# def exim ():
# 	c = csv.writer(open('data.csv','wb'))
# 	# for item in g_data:
# 	c.writerow(["business_name","streetAddress","addressLocality","addressRegion","postalCode"])
# 	c.writerow([list_info])
# # exim()