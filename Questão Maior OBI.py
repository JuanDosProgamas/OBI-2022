n= int(input())
m=int(input())
s= int(input())
ma=0
for i in range(n,m+1):
    if i==10000:
        d1=1
        if d1==s:
            ma = ma if ma != None and ma >  i else i
    elif 1000<i<=9999:
        d2=n//1000
        r2=n%1000
        
        d3=r2//100
        r3=r2%100
        
        d4=r3//10
        r4=r3%10

        d5=r4//1
        r5=r4%1
        if d2+d3+d4+d5==s:
            ma = ma if ma != None and ma >  i else i
    elif 100<=i<=999:
        d3=i//100
        r3=i%100
        
        d4=r3//10
        r4=r3%10

        d5=r4//1
        r5=r4%1
        if d3+d4+d5==s:
            ma = ma if ma != None and ma >  i else i
    elif 10<=i<=99:
        d4=i//10
        r4=i%10

        d5=r4//1
        r5=r4%1
        if d4+d5==s:
            ma = ma if ma != None and ma >  i else i
    elif 1<=i<=9:
        d5=i//1
        r5=i%1
        if d5==s:
            ma = ma if ma != None and ma >  i else i
if ma==0:
    print(int(-1))
else:
    print(ma)


