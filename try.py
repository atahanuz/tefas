import http.client
import ssl
from bs4 import BeautifulSoup

finaltext = ""
baseurl = "www.tefas.gov.tr"
url = "/FonAnaliz.aspx?FonKod=MAC"  # replace 'MAC' with the actual name you want

# Create a new SSL context
context = ssl._create_unverified_context()

# Use the context to create a connection
conn = http.client.HTTPSConnection(baseurl, context=context)

# Send a GET request
conn.request("GET", url)

# Get the response
res = conn.getresponse()
data = res.read()

soup = BeautifulSoup(data, "html.parser")
all_text = ''.join(soup.stripped_strings)

# first 1000 characters of the string
finaltext = all_text[500:800]

print(finaltext)
