from unittest import TestCase
import Task202
import distance
# encoding: utf-8


class TestLevenshtein(TestCase):
    cases = [['ночь', 'дочь'], ['', 'день'],['дочка', 'ор'],['день', 'день'],['олень', 'день'],['день', 'day']]

 #   def test_getDistance(self,word1,word2):
  #      self.fail()



    def testLev(self):
        b=Task202.Levenshtein()
        for i in self.cases:
            self.assertEqual(b.getDistance(i[0],i[1]),distance.levenshtein(i[0],i[1]))
            print(b.getDistance(i[0],i[1]))
