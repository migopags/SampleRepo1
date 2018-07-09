string = 'hello, good morning, hello'

def kaltas(word):
	newWord = ''
	for w in word:
		if w.isalpha():
			newWord += w
	return newWord

def ngram(sentence, n):
	words = sentence.lower().split(' ')
	for i in range(len(words)):
		words[i] = kaltas(words[i])
	end = n
	grams = {}git
	while end <= len(words):
		# words[end-n:n]
		if grams.has_key(words[end-n:n]):
			grams[words[end-n:n]] += 1
		else:
			grams[words[end-n:n]] = 1
	print(grams)

sentence = 'betty botter had some butter. but, she said, this batter is bitter. if i bake this bitter butter, it will make my batter bitter!'
ngram(sentence, 1)