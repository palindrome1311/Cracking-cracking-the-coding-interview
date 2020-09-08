def powerset(s):
    x=len(s)
    for i in range(1<<x):
        for j in range(x):
            if(i & ( 1<<j )):
                print(s[j],end="")
        print("")

powerset([4,6,5])