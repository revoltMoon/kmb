import re, string
def workWithText():
	text = readText()
	text = text.lower()
	f = open('anacondaResult.txt', 'w')
	f.write(str(len(re.findall(r"[\n']+?", text))) + '\n')
	f.write(re.sub(r'\bsnake', 'python', text) + '\n')
	text = re.sub(r'\bsnake', 'python', text)
	count = len(text)
	f.write('\n\n\n')
	sentence = ""
	for i in range(count):
		if text[i] != ".":
			sentence = sentence +  text[i]
		else:
			if (sentence.find("python",0 , len(sentence)) != -1) and (sentence.find("anaconda",0,len(sentence)) != -1):
				f.write(sentence + '\n')
			sentence = ""
	#second b task
	years = re.findall(r'\d{4}', text)
	second = open('secondB.txt', 'w')
	years = sorted(years)
	for year in years:
		second.write(year + ' ')
	second.close()
	lst = re.sub('[%s]' % re.escape(string.punctuation), '', text)
	lst = re.sub('[%s]' % re.escape("\n"), '', lst)
	lst = re.sub(r"\d", '', lst)
	words = lst.split(' ')
	words = sorted(words)
	words = deleteRepeats(words)
	del words[0]
	third = open('secondA.txt', 'w')
	for word in words:
		third.write(word + ' ')
	third.close()
	f.close()

def deleteRepeats(words):
	result = []
	for i in words:
		if i not in result:
			result.append(i)
	return result
def readText():
	f = open('anaconda.txt', 'r',encoding="utf-8")
	text = f.read()
	f.close()
	return text



if (__name__ == '__main__'):
	workWithText()