f1 = open('OpenMe.mp3')
f2 = open('OpenMe.txt', 'w')
f2.write(f1.read())
f1.close()
f2.close()
