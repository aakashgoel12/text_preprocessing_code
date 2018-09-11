sample_string = "All emotions, and that one particularly, were abhorrent to his cold, precise but admirably balanced mind."

########################
### CASE CONVERSION ####
########################

def case_conversion(sample_string):
	# convert string into lower
	sample_string_lower = sample_string.lower()
	# convert string into upper
	sample_string_upper = sample_string.upper()
	return sample_string_lower

sample_string_lower = case_conversion(sample_string)

print("Original string is \n{}".format(sample_string))
print("\n")
print("Lower case string is \n{}".format(sample_string_lower))

########################
### TOKENIZATION #######
########################

def tokenization(sample_string):
	from nltk.tokenize import word_tokenize
	tokens = word_tokenize(sample_string)
	return tokens

tokens = tokenization(sample_string)
print("Tokens in string \n{}".format(tokens))
print("\n\n")

########################
### REMOVE STOPWORDS ###
########################

def remove_stopword(sample_string):
	from nltk.corpus import stopwords
	lower_case_string = case_conversion(sample_string)
	lowered_tokens = tokenization(lower_case_string)
	language = 'english'
	stopwords = stopwords.words(language)
	print("Stopwords are: \n{}".format(stopwords))
	print("\n")
	lowered_filtered_tokens = list()
	for word in lowered_tokens:
		if word not in stopwords:
			lowered_filtered_tokens.append(word)
	lowered_filtered_string = " ".join(lowered_filtered_tokens)
	return lowered_filtered_string

filtered_string = remove_stopword(sample_string)

print("Before removing stopwords, string is \n{}".format(sample_string))
print("\n")
print("After removing stopwords, string is \n{}".format(filtered_string))

#######################################
### PART-OF-SPEECH TAGGING  ###########
#######################################

def get_pos_tag(sample_string):
	from nltk import pos_tag
	# pos_tag function takes token as input
	original_tokens = tokenization(sample_string)
	sample_string_tag = pos_tag(original_tokens)
	return sample_string_tag

sample_string_tag = get_pos_tag(sample_string)
print("String with part of speech tags \n{}".format(sample_string_tag))
print("\n")
pos_tag_url = "https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html"
print("Please check below url for defination of part of speech tags \n{}".format(pos_tag_url))

########################
### STEMMING ###########
########################

def stemming(sample_string):
	from nltk.stem import PorterStemmer
	stemmer = PorterStemmer()
	stemmed_string = ''
	original_tokens = tokenization(sample_string)
	for word in original_tokens:
		stemmed_string+=stemmer.stem(word)+' '
	stemmed_string = stemmed_string.strip()
	return stemmed_string

stemmed_string = stemming(sample_string)
print("Before performing stemming, original string is \n{}".format(sample_string))
print("\n")
print("After performing stemming, string converted into \n{}".format(stemmed_string))

#############################
### LEMMATIZATION ###########
#############################

def get_wordnet_pos(treebank_tag):
	from nltk.corpus import wordnet
	if treebank_tag.startswith('J'):
		return wordnet.ADJ
	elif treebank_tag.startswith('V'):
		return wordnet.VERB
	elif treebank_tag.startswith('N'):
		return wordnet.NOUN
	elif treebank_tag.startswith('R'):
		return wordnet.ADV
	else:
		return None

def lemmatization(sample_string):
	from nltk.stem.wordnet import WordNetLemmatizer
	lemmatizer = WordNetLemmatizer()
	sample_string_tag = get_pos_tag(sample_string)
	lemmatized_string = ''
	for word,tag in sample_string_tag:
		wntag = get_wordnet_pos(tag)
		if wntag is None:
			lemmatized_string+= lemmatizer.lemmatize(word)+' '
		else:
			lemmatized_string+= lemmatizer.lemmatize(word,pos=wntag)+' '
	lemmatized_string = lemmatized_string.strip()
	return lemmatized_string

lemmatized_string = lemmatization(sample_string)
print("Before performing lemmatization, original string is \n {}".format(sample_string))
print("\n")
print("After performing lemmatization, string converted into \n {}".format(lemmatized_string))
print("\n\n")

#############################
### KEEP ONLY ALPHABET ######
#############################

def keep_only_alphabet(sample_string):
	import re
	return re.sub(r'[^a-zA-Z\ ]+','',sample_string)

sample_string_alphabet = keep_only_alphabet(sample_string)

#############################
### WORD SEGMENTATION #######
#############################

def word_segment(word):
	import wordsegment as ws
	ws.load()
	return ws.segment(word)

word="goodhuman"
print(word_segment(word))