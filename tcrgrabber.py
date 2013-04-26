import urllib2,re

# Settings the minimum & maximum page number
minimum = 1
maximum = 8

# Initialize the regular expression to find all the MP3s Url
regExp = re.compile('http://media\.r-n-d\.net/audio/tcr/tcr[0-9]{6}\.mp3',re.IGNORECASE)

urls = []

for x in xrange(minimum,maximum):
	try:
		# Fetching the page
		urlHandler = urllib2.urlopen(urllib2.Request("http://www.thecityrises.com/page/"+str(x)+"/"))
		pageHtml = urlHandler.read()

		# Gathering the graal (the URL of the MP3s) and merging them to "urls"
		urls += regExp.findall(pageHtml)
		print "Page " + str(x) + " of " + str(maximum) + " scanned."
	except Exception:
		print "Something wrong happened"

	pass

# Removing the duplicates URLs
urls = list(set(urls))

print str(len(urls)) + " URLs found."

# Saving the URLs to a file
fileHandler = open("urls.txt","w")

for urlID in urls:
	fileHandler.write(urlID + "\n")

fileHandler.close()

print "Wrote all the URLs to \"urls.txt\"."