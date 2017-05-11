import httplib2
import urllib2
from bs4 import BeautifulSoup, SoupStrainer
import re

http = httplib2.Http()
website = 'http://www.bhu.ac.in/telephone/'
doc_links = []
emails = []

status, response = http.request(website)

for link in BeautifulSoup(response,"lxml", parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        if 'doc' in link['href']:
            doc_links.append(website+link['href'])

print "Got doc links.."
print doc_links

for i in doc_links:
    try:
        doc = urllib2.urlopen(i)
        doc_data = doc.read()
        match = match = re.findall(r'[\w\.-]+@[\w\.-]+', doc_data)
        emails.extend(match)
        print "done", i
    except Exception as e:
        print e

print 'Yo, got all emails'

print 'writing data in results.txt'
with open('results.txt', "w") as f:
    for email in emails:
        f.write(email)
        print(email)
        f.write("\n")
