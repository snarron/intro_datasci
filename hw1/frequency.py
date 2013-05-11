import sys
import json
from collections import Counter

def clean_tweet(tweet_file):
	new_tweet_file = tweet_file.readlines()
	#tweet_text = new_tweet_file.keys()
	#print new_tweet_file
	tweet_list = []
	for line in new_tweet_file:
		#print line
		tweet_text = json.loads(line)
		if tweet_text.get('text'):
			tweet_list.append(tweet_text)
			#print tweet_text
	return tweet_list

def tweet_word_count(clean_tweet_list):
	terms = []
	for i in clean_tweet_list:
		#print i
		split_list = i
		for i in split_list.get('text').split():
			terms.append(i)
			#print i

	#print terms
	total_term_count = len(terms)
	term_counter = Counter(terms)
	return_list = []
	for key in term_counter.keys():
		return_list.append((key, int(term_counter[key])/float(total_term_count)))
	return return_list

		
def main():
    tweet_file = open(sys.argv[1])
    clean_tweet_list = clean_tweet(tweet_file)
    #for i in clean_tweet_list:
    #	print i, '\n'
    
    #print tweet_word_count(clean_tweet_list)
    final_tweet_list = tweet_word_count(clean_tweet_list)
    for i in final_tweet_list:
    	print i[0], i[1]




if __name__ == '__main__':
    main()