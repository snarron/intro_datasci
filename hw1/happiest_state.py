import sys
import json
from collections import Counter
import string
from collections import Counter

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    return str(fp.readlines())


def read_sent(sent_file):
	# takes a txt file of sentiment scores as input,
	# returns a dictionary with a pair of
	# word:score
	sent_dict = dict()
	sent_read = sent_file.read()
	sent_json = sent_read.split('\n')
	for entry in sent_json:
		sent_dict.update({str(entry.split('\t')[0]):entry.split('\t')[-1]})
	return sent_dict

def pos_neg_analysis(words, sent_dict):
	pos = 0
	neg = 0
	counter = []
	scores = []

	for word in words:
		if word in sent_dict:
			counter.append((word, float(sent_dict.get(word))))
			scores.append(float(sent_dict.get(word)))
		else:
			pass

	for i in counter:
		if i[1] < 0:
			neg += 1
		elif i[1] > 0:
			pos += 1
		else:
			pass
	
	if len(scores) == 0:
		scores = [0]
	else:
		pass
	new_score = (pos-neg)*max(scores)

	return new_score

	
def read_tweet(tweet_file, sent_dict):
	tweet_read = tweet_file.readlines()

	state_tweet_list = []

	for i in tweet_read:
		load = json.loads(i.encode('utf-8'))
		location = load.get('place')
		language = load.get('lang')

		if location and location['country'] == "United States":
			state = location['full_name'].split(',')[1].encode('utf-8').split()
			if len(state) == 1:
				if load.get('text') == None:
					words = []
				else:
					words = [word.encode('utf-8').lower() for word in load.get('text').split()]
			else:
				words = []
		else:
			state = None
			words = []

		if state and state[0] != "US" and len(state[0]) == 2:
			state_tweet_list.append((state[0], words))
	return state_tweet_list
		#print words

def state_score(state_tuple, sentiment_dictionary):
	state = state_tuple[0]
	words = state_tuple[1]
	
	result_dict = {}
	
	# Print each word in a tweet if tweet 'text' is not None
	new_word_score = pos_neg_analysis(words, sentiment_dictionary)
	score = 0

	for word in words:
		if word in sentiment_dictionary:
			score += int(sentiment_dictionary[word])
		else:
			score += int(new_word_score)
		#	print "%s \t %s" % (word, new_word_score)
	if state in result_dict.keys():
		result_dict[state] += score
	else:
		result_dict[state] = score
	result_dict.update({state:score})
	return result_dict

def happy_states(result_list):
	state_dict = {}	
	for i in result_list:
		state, score = i[0], i[1]
		if state in state_dict.keys():
			state_dict[state] += score
		else:
			state_dict[state] = score

	top_states = []

	for w in sorted(state_dict, key=state_dict.get, reverse=True):
  		top_states.append(w)#, state_dict[w]
	return top_states[0]


	


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sent_dictionary = read_sent(sent_file)

    intermediate_result = read_tweet(tweet_file, sent_dictionary)

    each_tweet_state = []
    for i in intermediate_result:
    	each_tweet_state.append(state_score(i, sent_dictionary).items()[0])
    
    final_result = happy_states(each_tweet_state)
    print final_result

if __name__ == '__main__':
    main()