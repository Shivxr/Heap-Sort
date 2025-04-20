def parent(ind):
    z=(ind-1)//2
    if z>=0:
        return z
    return -1
def left(ind,ln):
    z=ind*2+1
    if z<ln:
        return z
    return -1
    
def right(ind,ln):
    z=ind*2+2
    if z<ln:
        return z
    return -1

def comp(ind,hp,ln):
    l,r=left(ind,ln),right(ind,ln)
    if (l,r)==(-1,-1):
        return -1
    elif l==-1 and r!=-1:
        if hp[r]<hp[ind]:
            return r
    elif l!=-1 and r==-1:
        if hp[l]<hp[ind]:
            print(3)
            return l
    elif l!=-1 and r!=-1:
        x=-1
        if hp[r]<hp[l]:
            x=r
        else:
            x=l
        if x!=-1 and hp[x]<hp[ind]:
            return x
    return -1
        
def hsort(hp):
    p=len(hp)-1
    sub=1
    while p>0:
        s=0
        hp[s],hp[p]=hp[p],hp[s]
        while comp(s,hp,len(hp)-sub)!=-1:
            z=comp(s,hp,len(hp)-sub)
            hp[s],hp[z]=hp[z],hp[s]
            s=z
        p-=1
        sub+=1
    return hp
            
        
    
def heapify(arr):
    hp=[]
    for i in range(len(arr)):
        hp.append(arr[i])
        
        while parent(i)!=-1 and hp[parent(i)]>hp[i]:
            hp[parent(i)],hp[i]=hp[i],hp[parent(i)]
            i=parent(i)
    return hp
    
arr=[2,5,1,3,4,8,6,7]
op=heapify(arr)
print(hsort(op))
