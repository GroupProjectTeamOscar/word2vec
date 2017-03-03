import nltk, collections, csv, tkinter as tk

#set number of words in vocabulary
VOC_SIZE = 50 * 1000

def addSpaceAfterPunctuation(text):
	punctuation = "!?."	
	out = ''
	for i in range(len(text)):
		out += text[i]
		if text[i] in punctuation and i+1 < len(text) and text[i+1] != ' ' and  not text[i+1] in punctuation:
			out += ' '
	return out

occuring_words = []


def build_vocabulary(text):
	global occuring_words

	tokens = nltk.word_tokenize(text)
	if ',' in tokens:
		tokens.remove(',')
	
	occuring_words += tokens
	

def mapWords2Numbers(words,vocabulary_size):
	#assign numbers according to frequency of word (1 to most common word, 2 to second most common, ...)
	dictionary = dict(collections.Counter(words).most_common(vocabulary_size-1))

	reverse_dictionary = dict(zip(dictionary.values(),dictionary.keys()))

	return dictionary, reverse_dictionary

"""
def processSentence(setnece, dictionary):
	tokens = nltk.word_tokenize(sentence)
	if ',' in tokens:
		tokens.remove(',')
"""

	



"""

#receive block of text, split it into sentences and call fucntion to process each sentence
def processBlockOfText(text,dictionary):
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	sentences = tokenizer.tokenize(addSpaceAfterPunctuation(text))
	for sentence in sentences:
		print(sentence,"\n\n")
		#processSentence(sentence,dictionary)
"""


def runPreprocessor():
	#select .csv file
	filename = tk.filedialog.askopenfilename()
	#read the file and generate output vector for Word2Vec neural network
	with open(filename,newline='') as csvfile:
		reader = csv.reader(csvfile,dialect='excel')
		
		#in first pass of the data extarct all the words and punctuation to build vocabulary
		first = True
		for row in reader:
			#skip first row in .csv file
			if first:
				first = False
				continue
			build_vocabulary(row[2])

	dictionary, reverse_dictionary = mapWords2Numbers(occuring_words, VOC_SIZE)
	
	data = []
	for word in occuring_words:
		data.append(dictionary[word])

	return data, dictionary, reverse_dictionary, VOC_SIZE

		
