import mmap
import bs4
import sys
import webbrowser
import requests
import re

def mapIt():
	if len(sys.argv) > 1:
	#get address from command line
		address = ''.join(sys.argv[1])
	else:
		address = 'Lawrence Street Center, Denver, CO'

	webbrowser.open('https://www.google.com/maps/place/'+address)
#finding websites which contain the information we are looking for
def webGet(url):
	webpage = requests.get(url)
	try:
		webpage.raise_for_status()
	except Exception as e:
		print('There was a problem with the url {}'.format(e))
	return webpage
#printing directly from the site
def printToFile(url, filename):
	webpage = webGet(url)
	webFile = open(filename, 'wb')

	for chunk in webpage.iter_content(10000):
		webFile.write(chunk)
#This function formats the html into the style we select
def formattedHTML(filename, formattedFilename):
	file = open(filename, 'r+')
	data = mmap.mmap(file.fileno(), 0)
	html = bs4.BeautifulSoup(data, 'html.parser')
	formatted = html.prettify('utf-8')
	formattedFile=open(formattedFilename, 'wb')
	formattedFile.write(formatted)
	formattedFile.close()
#finding specific entries within the files we are scraping
def parseHTML(filename, searchWord, numWordsBefore, numWordsAfter):
	
	print('***Searching in {} for the keyword {}***'.format(filename, searchWord))
	file = open(filename, 'r+')
	data = mmap.mmap(file.fileno(), 0)

	regexString = '(\\S+\\s+)'
	regexString = regexString + "{" + str(numWordsBefore) + "}"
	regexString = regexString + '\\b' + searchWord + '\\b' + '(\\S+\\s+)'
	regexString = regexString + '{' + str(numWordsAfter) + '}'

	for match in re.finditer(regexString, data.read().decode('utf-8')):
		print('Start:{}, End:{}\n\n{}'.format(match.start(), match.end(), match.group()))
	file.close()
#using bs4 to grab text
def justText(filename):
	file = open(filename, 'r+')
	data = mmap.mmap(file.fileno(), 0) #memory map handles the memory for large file, acts like a string
	html = bs4.BeautifulSoup(data, 'html.parser')
	text = html.get_text()
	print(text)

def justLinks(filename):
	file = open(filename, 'r+')
	data = mmap.mmap(file.fileno(), 0)
	html = bs4.BeautifulSoup(data, 'html.parser')
	links = html.findAll('a', href=True)
	for link in links:
		if link['href'].startswith('http'):
			print(link)

def postToForm():
	header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
	r = requests.post('http://localhost/csci5742.php', data={'name':'Lucas Fulmer','movie':'Hello World'}, headers=header)
	print(r.text)
	print(r.headers)





if __name__ == '__main__':
    
    printToFile('https://automatetheboringstuff.com/files/rj.txt', 'RomeoAndJuliet.txt')
    printToFile('https://en.wikipedia.org/wiki/Computer_security', 'wiki.html')

    parseHTML('RomeoAndJuliet.txt', 'Juliet', 4,4)
    parseHTML('wiki.html', 'security', 4,4)
    justText('wiki.html')
    justLinks('wiki.html')
    formattedHTML('wiki.html', 'wikipretty.html')
    
    postToForm()
else:
    print("imported rather than run directly")

