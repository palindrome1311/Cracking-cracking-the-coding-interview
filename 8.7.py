def getPerm(prefix,rem,result):
    if(len(rem)==0):    
        result.append(prefix)
    
    for i in range(len(rem)):
        before = rem[:i]
        after = rem[i+1:]
        c = rem[i]
        getPerm(prefix+c, before + after, result)


str1 = "ABCD"
result=[]
getPerm("",str1,result)
print(result)
