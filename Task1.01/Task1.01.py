__author__ = 'sf2016'

# encoding: utf-8
import random
from string import punctuation




def randomizer(text):
    buffer=list(text[1:-1])
    random.shuffle(buffer)
    buffer.insert(0,text[0])
    if len(text)!=1:
        buffer.append(text[-1])
    text1=''.join(buffer)
    return text1

def parser(text):
    firstPart=[]
    lastLatterIndex=0
    for i in text:
        if i not in punctuation:
            firstPart.append(i)
            lastLatterIndex += 1
        else:
            break
    secondPart=text[lastLatterIndex:]
    text1=[]
    text1.append(''.join(randomizer(firstPart)))
    text1.append(''.join(secondPart))
    result=''.join(text1)
    return result


text="По результатам исследований одного английского института не имеет значения в каком порядке идут слова"
text="вот результат: результат"
bufferedText=text.split()
for i in bufferedText:
    print(parser(i),end=" ")


