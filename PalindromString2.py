str ="CTC"
strR=""
strL=len(str)
for i in range(strL):
    strR+=str[strL-1]
    strL-= 1
    if strL==0:
        break
print(strR)

string = "Hello, World!"
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print(reversed_string)  # Output: !dlroW ,olleH
