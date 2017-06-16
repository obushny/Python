# encoding: utf-8

import distance
class Levenshtein:

    def getDistance(self,word1,word2):
        wordList1=list(word1)
        wordList2=list(word2)

        if len(wordList1)==0 or len(wordList2)==0:
            x=max(len(wordList1),len(wordList2))

        else:
            if wordList1[-1]==wordList2[-1]:
                equity=0
            else:
                equity=1
            x=min(
                self.getDistance(''.join(wordList1[:-1]),''.join(wordList2))+1,
                self.getDistance(''.join(wordList1), ''.join(wordList2[:-1])) + 1,
                self.getDistance(''.join(wordList1[:-1]), ''.join(wordList2[:-1])) + equity
            )
        return x

#print(distance.levenshtein('достопримечательность','примечательный'))
#print(Levenshtein().getDistance('ечательный','ечательный'))

#'достопримечательность','примечательный'