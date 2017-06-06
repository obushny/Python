__author__ = 'sf2016'
a=[50, 1, 2, 5, 17, 0, 45, 5]
maxIndex=a.index(max(a))
minIndex=a.index(min(a))
if maxIndex<minIndex:
    start=maxIndex
    finish=minIndex
else:
    start=minIndex
    finish=maxIndex
sum=0
i=start+1
while i<finish:
    sum += a[i]
    i += 1
print(sum)
