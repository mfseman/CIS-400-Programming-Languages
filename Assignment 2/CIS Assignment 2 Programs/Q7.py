import urllib.request
from bs4 import BeautifulSoup

# URL:
URL = "https://www.tandfonline.com/toc/tjms20/current"

#Extract HTML Tags from website using beutiful soup
htmlTags = urllib.request.urlopen(URL).read()
soup = BeautifulSoup(htmlTags)

# Remove scripts and css
for script in soup(["script", "style"]):
    script.extract()

# retrieve text from the website and place it in text
text = soup.get_text()

# Take the lines, and delete them that have spacces between them
lines = (line.strip() for line in text.splitlines())

# Display in multiple lines using split
split = (phrase.strip() for line in lines for phrase in line.split("  "))
# remove any blank lines
text = '\n'.join(splitting for splitting in split if splitting)
sorted(text, reverse=True)
print(text)