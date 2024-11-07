num=int(input("enter a number"))
count=0
for i in range(1, num + 1):  #for start loop 1 and end upto num so num+1 as num is exclusive
    if num%i==0:
        count+=1
if count == 2:
    print("It's prime")
else:
    print("It's not prime")
