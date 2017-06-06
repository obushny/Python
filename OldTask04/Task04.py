__author__ = 'sf2016'
a=[100,50, 1, 0, -2, -5, 17, 0, 45, 5]
start=a.index(0)
finish=a[start+1:].index(0)+start+1
counter=0
for i in a[start+1:finish]:
    if i<0:
        counter += 1
print(counter)

# Не обрабатывается исключение, когда не нашлось два 0