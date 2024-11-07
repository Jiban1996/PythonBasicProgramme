str ="CTC"
strR=""
strL=len(str)
for i in range(strL):
    strR+=str[strL-1]
    strL-= 1
    if strL==0:
        break
print(strR)
