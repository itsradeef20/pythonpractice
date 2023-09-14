a=int(input())

if 0 <= a <200000000:
    list=[]
    if a >999:
        e=a%1000
        list.append(e)
        q=a/1000
        #print(e)
        if q>999:
            w=int(q%1000)
            list.append(w)
            s=int(q/1000)
            list.append(s)
            #print(w)
               # print(d)

g=str(list[2])+","+str(list[1])+","+str(list[0]) 

print(g)