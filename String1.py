s=input("Enter String : ")

al=0
n=0
sp=0
uc=0
lc=0
spc=0
for i in s:
    if i.isalpha():
        al=al+1
    elif i.isnumeric():
        n=n+1
    elif i.isspace():
        sp=sp+1
    else:
        spc=spc+1
    if i.isupper():
        uc=uc+1
    elif i.islower():
        lc=lc+1

print("Total Alphabets : ",al)
print("Total Numeric : ",n)
print("Total Space : ",sp)
print("Total Upper Case : ",uc)
print("Total Lower Case : ",lc)
print("Total Special Character : ",spc)
