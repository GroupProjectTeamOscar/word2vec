import nltk, collections, csv, tkinter as tk

def build_vocabulary(words,vocabulary_size):
	#assign numbers according to frequency of word (1 to most common word, 2 to second most common, ...)
	dictionary = collections.Counter(words).most_common(vocabulary_size-1)

	reverse_dictionary = dict(zip(dictionary.values(),dictionary.keys()))

	return dictionary, reverse_dictionary


#def processSentence(setnece_vector, ):



#receive block of text, split it into sentences and call fucntion to process each sentence
def processBlockOfText(text):
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	sentences = tokenizer.tokenize(text,realign_boundraries=True)
	for sentence in sentences:
		print(sentence)
		#processSentence(sentence)

#select .csv file
filename = tk.filedialog.askopenfilename()

#read the file and generate output vector for Word2Vec neural network
with open(filename,newline='') as csvfile:
	reader = csv.reader(csvfile)
	
	first = True
	for row in reader:
		#skip first row in .csv file
		if first:
			first = False
			continue
		processBlockOfText(row[2])
		break
