import re
from datetime import datetime
def workWithText():
	text = openText()
	separatedNews = text.split('-----------')
	dates = re.findall(r"\d{2}\.\d{2}\.\d{4}, \d{2}:\d{2}", text)
	dateList = []
	for i in range(len(dates)):
		dates[i] = dates[i].replace('.', " ")
		dates[i] = re.sub('[%s]' % re.escape(","), '', dates[i])
		dateList.append(datetime.strptime(dates[i], '%d %m %Y %H:%M'))
	dateList = sorted(dateList)
	for i in range(len(dates)):
		for m in range(i, len(dates)):
		 	if separatedNews[m].find(dateList[i].strftime("%d.%m.%Y, %H:%M")) != -1:
		 		separatedNews[m],separatedNews[i] = separatedNews[i],separatedNews[m]
	f = open('thirdTask.txt', 'w')
	for i in range(len(separatedNews)):
		f.write(separatedNews[i])
	f.close()





def openText():
	f = open('News.txt', 'r',encoding="utf-8")
	text = f.read()
	f.close()
	return text



if (__name__ == '__main__'):
	workWithText()