__author__ = 'sf2016'
# encoding: utf-8
import distance


class Levenshtein:

    def defineDistanse(self,a, b):
        listA = list(a)
        listB = list(b)
        if len(listA) == 0 or len(listB) == 0:
            x = max(len(listA), len(listB))
        else:
            if listA[-1] == listB[-1]:
                equity = 0
            else:
                equity = 1
            x = min(
                self.defineDistanse(listA[:-1], listB) + 1,
                self.defineDistanse(listA, listB[:-1]) + 1,
                self.defineDistanse(listA[:-1], listB[:-1]) + equity
            )
        return x


word1="ночь"
word2="дочка"
a = Levenshtein()
print(a.defineDistanse(word1,word2))
print(distance.levenshtein(word1,word2))


