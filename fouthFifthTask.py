import re
import pymorphy2
def workWithText():
	text = openText()
	text = text.lower()
	text = re.sub(re.escape("автор"), '', text)
	text = re.sub(re.escape("дата"), '', text)
	text = re.sub(r"\d{2}\.\d{2}\.\d{4}, \d{2}:\d{2}", '', text)
	text = re.sub(re.escape(r"-----------"), '', text)
	text = re.sub(re.escape(r"________________"), '', text)
	text = re.sub(re.escape(r":"), '', text)
	text = re.sub("—", '', text)
	text = re.sub("–", '', text)
	text = re.sub(r"\d{4}", '', text)
	words = text.split()
	functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP'}
	text2 = [word for word in words if pos(word) not in functors_pos]
	frequency = {}
	for word in text2:
		count = frequency.get(word,0)
		frequency[word] = count + 1
	list_of_sorted_pairs = [(k, frequency[k]) for k in sorted(frequency.keys(), key=frequency.get, reverse=True)]
	f = open('fouthAnswer.txt', 'w')
	result = [x[0] for x in list_of_sorted_pairs]
	for i in range(0, 30):
		f.write(result[i] + "\n")
	f.close()
	#task 5
	f = open('fifthAnswer.txt', 'w')
	for i in range(0, 5):
		phrase = re.findall(result[i] + r' \w+', text)
		phrase = sorted(phrase)
		for words in phrase:
			f.write(words + '\n')
		phraseCount = dict((x, phrase.count(x)) for x in set(phrase) if phrase.count(x) > 1)
		f.write('\n\n---------\n\n')
		for phrases, counter in phraseCount.items():
			f.write(phrases + ': ' + str(counter) + '\n')
		f.write('\n\n---------\n\n')
	f.close()


def pos(word, morth=pymorphy2.MorphAnalyzer()):
    return morth.parse(word)[0].tag.POS


def openText():
	f = open('News.txt', 'r',encoding="utf-8")
	text = f.read()
	f.close()
	return text



if (__name__ == '__main__'):
	workWithText()