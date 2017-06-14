from unittest import TestCase
from Task2 import Levenshtein
import distance
# encoding: utf-8
__author__ = 'sf2016'


class TestLevenshtein(TestCase):
  def test_defineDistanse(self,word1,word2):
    self.word1=word1
    self.word2=word2
    a=Levenshtein()
    self.assertEqual(a.defineDistanse(word1,word2),distance.levenshtein(word1,word2))
    #self.fail()

a=TestLevenshtein()
a.test_defineDistanse('day','days')


#tests={['day','days'], ['day','dare'], ['','day'], ['',''], ['day','day']}

#for i in tests:
 # TestLevenshtein.test_defineDistanse(i[0],i[1])

