import sys
import json
from collections import Counter

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    return str(fp.readlines())


def read_sent(sent_file):
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



	
def read_tweet(tweet_file, sentiment_file):
	sentiment_dictionary = read_sent(sentiment_file)
	tweet_read = tweet_file.readlines()


	result_list = {}
	for i in tweet_read:
		load = json.loads(i.encode('utf-8'))
		if load.get('text') == None:
			words = []
		else:
			words = [word.encode('utf-8') for word in load.get('text').split()]
		#print words

		# Print each word in a tweet if tweet 'text' is not None
		new_word_score = pos_neg_analysis(words, sentiment_dictionary)
		score = 0
		for word in words:
			if word in sentiment_dictionary:
				print "%s %s" % (word, sentiment_dictionary[word])
			else:
				print "%s %s" % (word, new_word_score)

				
    		

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    #read_sent(sent_file)
    #sentiment_dictionary = read_sent(sent_file)
    final_result = read_tweet(tweet_file, sent_file)
    return final_result
    #print sentiment_dictionary
    #for i in final_result:
    #	print i, final_result[i]


if __name__ == '__main__':
    main()