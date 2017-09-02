#Emily Murphy
#2017-09-01
#stringAnalysis.py - takes sentence as input and reports how many words and cahracters the sentence has

s1 = input('Enter sentence: ')
chara = input('Enter a character to search for: ')
words = int(len(s1.split()))
charac = int(len(s1))
print('Your sentence has', words, 'words and', charac, 'characters and', int(charac - words) + 1, 'letters')
print('Your sentence has', int(s1.count(chara)), 'of the character', chara)
word = input('Enter a word to search for: ')
print('Your sentence has', int(s1.count(word)), 'of the word', word)
