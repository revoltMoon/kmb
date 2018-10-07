import re
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

			
	f.close()



def readText():
	f = open('anaconda.txt', 'r',encoding="utf-8")
	text = f.read()
	f.close()
	return text

workWithText()