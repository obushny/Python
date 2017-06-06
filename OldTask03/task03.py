__author__ = 'sf2016'
a=[0,50, 1, 0, 2, 5, 17, 0, 45, 5]
index=len(a)-1
counter=0
sum=0
while index>0:
    if a[index]==0: break
    else:
        counter +=1
        sum +=a[index]
        index -= 1
if counter == 0: print("There is no numbers after zero")
elif index == 0:
    if(a[0] == 0): print(sum/counter)
    else: print("There is no zero in list")
else: print(sum/counter)

