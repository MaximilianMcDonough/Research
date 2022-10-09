import requests
import re
from bs4 import BeautifulSoup
#from gensim.summarization import summarize

# WikiPage is a class that gets information from the html of a wikipidia url


class Wikipedia:

	def __init__(self, word):

		#getting the html from the given url
		url = 'https://en.wikipedia.org/wiki/' + word
		html = requests.get(url)
		self.soup = BeautifulSoup(html.text, features="html.parser")
		self.soup.find("div", {'class':'reflist'}).replace_with('')
	#----------------------------------------------------------------------------------------------------------------------------------------


	# gets the links from the html
	def get_links(self):
		links = []

		for link in self.soup.find(id='bodyContent').find_all('a'):
			text = str(link.text)
			href = str(link.get('href'))

			# not a hidden link, external link, or wierd .sgv, .png link
			if(text !=  None and '/wiki/' in href and '.' not in href):
				href = 'https://en.wikipedia.org' + href
				links.append((text, href))

		return links
	#-----------------------------------------------------------------

	# gets the text from the html
	def getText(self):
		text = ''

		for p in self.soup.find(id='bodyContent').find_all('p'):
			text += ' ' + p.get_text()

		return text
	#------------------------------------------------------------------

	# gets the headers from the html
	def getHeaders(self):
		headers = []

		for h in self.soup.find(id='bodyContent').find_all('h2'):
			headers.append(h.text)

		for h in self.soup.find(id='bodyContent').find_all('h3'):
			headers.append(h.text)

		return headers[1:]
	#-------------------------------------------------------------------

	def getSources(self):
		sources = []
		for source in self.soup.find_all('cite'):
			sources.append(source.text)

		return sources

	def trim_text(self):
		zipfs_law = ['the','of',
		'and',
		'to',
		'a',
		'in',
		'is',
		'that',
		'was',
		'it',
		'for',
		'on',
		'with',
		'he',
		'be',
		'I',
		'by',
		'as',
		'at',
		'you',
		'are',
		'his',
		'had',
		'not',
		'this',
		'have',
		'from',
		'but',
		'which',
		'she',
		'they',
		'or',
		'an',
		'her',
		'were'
		'there',
		'we',
		'their',
		'been',
		'has',
		'will',
		'one',
		'all',
		'would',
		'can',
		'if',
		'who',
		'more',
		'when',
		'said',
		'do',
		'what',
		'about',
		'its',
		'so',
		'up',
		'into',
		'no',
		'him',
		'some',
		'could',
		'them',
		'only',
		'time',
		'out',
		'my',
		'two',
		'other',
		'then',
		'may',
		'over',
		'also',
		'new',
		'like',
		'these',
		'me',
		'after',
		'first',
		'your',
		'did',
		'now',
		'any',
		'people',
		'than',
		'should',
		'very',
		'most',
		'see',
		'where',
		'just',
		'made',
		'between',
		'back',
		'way',
		'many',
		'years',
		'being',
		'our',
		'how',
		'work']

		text = self.getText()

		for word in zipfs_law:
			word = ' ' + word + ' '
			regular_expression = re.compile(re.escape(word), re.IGNORECASE)
			text = re.sub(regular_expression, ' ', text)

		return text


class Wiktionary:

	def __init__(self, word):
		#getting the html from the given url
		url = 'https://en.wiktionary.org/wiki/' + word
		html = requests.get(url)
		self.soup = BeautifulSoup(html.text, features="html.parser")
		

	def getDefs(self):
		definitions = [[]]

		for definition in self.soup.find_all('ol'):
			definitions.append(definition.text)

		return definitions

	def getQuotes(self):
		pass


class Wikisource:

	def __init__(self, word):
		#getting the html from the given url
		url = 'https://en.wikisource.org/wiki/' + word
		html = requests.get(url)
		self.soup = BeautifulSoup(html.text, features="html.parser")

	def getSources():
		sources = []

		for source in self.soup.find_all():
			pass

class Wikiquote:

	def __init__(self, word):
		#getting the html from the given url
		url = 'https://en.wikiquote.org/wiki/' + word
		html = requests.get(url)
		self.soup = BeautifulSoup(html.text, features="html.parser")
	

	def getQuotes(self):
		quotes = []

		for quote in self.soup.find(id='bodyContent').find_all('li'):
			quotes.append(quote.text)

		return quotes

class GoogleSearch:

	def __init__(self, word):
		url = 'https://google.com/search?q=' + word + '?'
		html = requests.get(url)
		self.soup = BeautifulSoup(html.content, features='html.parser')
		print(self.soup)


	def getUrls(self):
		urls = []

		for url in self.soup.find('div', id="search").find_all('h3', clas='LC20lb MBeuO DKV0Md'):
			urla.append(url)

		print(urls)


class RefSeek:

	def __init__(self, word):
		url = 'https://www.refseek.com/search?q=' + word
		html = requests.get(url)
		self.soup = BeautifulSoup(html.text, features='html.parser')
		self.links = self.getLinks()

	def getLinks(self):
		links = []

		for a in self.soup.find('div', class_='main__content').find_all('div', class_='sticky__title'):
			link = a.find('a').get('href')

			if link.find('http') == -1:
				link = 'https://www.refseek.com' + link

			links.append(link)

		return(links)

	def getText(self):
		text = []

		for link in self.links:
			html = requests.get(link)
			s = BeautifulSoup(html.text, features='html.parser')
			text.append(s.text)

		return(text)

class ISBNSearch:

	def __init__(self, word):
		url = 'https://isbndb.com/search/books/' + word
		html = requests.get(url)
		self.soup = BeautifulSoup(html.text, features='html.parser')

	def getBooks(self):
		books = []
		for h2 in self.soup.find_all('h2', class_='search-result-title'):
			books.append(h2.text)

		return(books)

