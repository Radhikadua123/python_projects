import time
import webbrowser

total_breaks = 3
count=0

print ("This program started on "+time.ctime())
while(total_breaks > count):
	webbrowser.open("https://www.youtube.com/watch?v=F_9TxX6nnFg")
	time.sleep(60)
	count=count+1

