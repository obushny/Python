__author__ = 'sf2016'

# encoding: utf-8
import random
from string import punctuation
from string import digits

def randomizer(text):
    if len(text)<2:
        buffer=text
    else:
        buffer=list(text[1:-1])
        random.shuffle(buffer)
        buffer.insert(0,text[0])
        buffer.append(text[-1])
    return ''.join(buffer)

def analizer(text):
    buffer=[]
    temp=[]
    for i in text:
        if (i not in punctuation) and (i not in digits):
            buffer.append(i)
        else:
            bufferedText=randomizer(''.join(buffer))
            temp.append(bufferedText)
            temp.append(i)
            buffer=[]
    temp.append(randomizer(''.join(buffer)))
    return ''.join(temp)

text="По результатам усследований одного английского университета, не имеет значения, "
text += 'в каком порядке расположены слова в слове. Главное, чтобы первая и последняя буквы были на месте. '
text += 'Остальные буквы могут следовать в полном беспорядке, все равно текст читается без проблем. '
text += 'Причиной этого является то, что мы не читаем каждую букву по отдельности, а все слово целиком'

bufferedText=text.split()
for i in bufferedText:
    print(analizer(i),end=" ")


