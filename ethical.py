from WikiPages import *
import Sumarazation as sum

topic = 'herodotus'

wikipedia = Wikipedia(topic)
wikiquote = Wikiquote(topic)
wikisource = Wikisource(topic)
wiktionary = Wiktionary(topic)
isbn = ISBNSearch(topic)

overview = sum.sumerize(wikipedia.getText(), 5)
definitions = wiktionary.getDefs()
testimonials = wikiquote.getQuotes()
sources = wikipedia.getSources()
#sources.append()
alussions = isbn.getBooks()
statistics = 'https://unstats.un.org/UNSDWebsite'
mainPoints = wikipedia.getHeaders()
humor = ''

def printReasearch():
	print(topic)
	print()

	print('Overiew:')
	print(overview)
	print()

	print('main points:')
	print(mainPoints)
	print()

	print('definitions:')
	print(definitions)
	print()

	print('testimonials:')
	print(testimonials)
	print()

	print('humor:')
	print(humor)
	print()

	print('alussions:')
	print(alussions)
	print()

	print('statistics:')
	print(statistics)
	print()

	print('sources:')
	print(sources)

printReasearch()