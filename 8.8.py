def getPerms(map,prefix,rem,result):
    if(rem==0):
        result.append(prefix)
        return
    
    for c in map.keys():
        count = map[c]
        if(count>0):
            map[c]-=1
            getPerms(map,prefix+c,rem-1,result)
            map[c]+=1

string = "AABBC"
dict1={}
for i in string:
    if i not in dict1.keys():
        dict1[i]=1
    else:
        dict1[i]+=1
result=[]

getPerms(dict1,"",len(string),result)

print(result)