__author__ = 'sf2016'
a=[0,50, 1, 0, -2, -5, 17, 0, 45, 5]
start=a.index(max(a))
index=len(a)-1
while index>start:
    if a[index]==0:
        del a[index]
    index -= 1
print(a)