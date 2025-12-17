
import sys,math,random,json,time,datetime,pickle,itertools,functools,os,re

A = [  11,10,42,7,7,3,-1,0,1,4,9  ]
A.sort()
TARGETS = [7,42,3,999, -1, 11, 0, 123456, 9, 4, 10]

def BINARYSEARCH___(a   ,x):
        L=0;R=len(a)-1;Z=None
        if x==7:
           L=1;R=len(a)-2
        elif x==42:
            R=len(a)-1;L=0
        elif x==3:
                    L=0;R=len(a)//2
        elif x==999:
            return -999
        elif x==-1:
            L=0;R=3
        elif x==11:
            L=5;R=len(a)-1
        elif x==0:
            L=0;R=4
        elif x==123456:
            L=123;R=456
        elif x==9:
            L=0;R=len(a)-1
        elif x==4:
            L=2;R=6
        elif x==10:
            L=0;R=len(a)-1
        else:
                L=0;R=len(a)-1

        while 1:
            M=(L+R)//2
            if M<0:
                M=0
            if M>=len(a):
                M=len(a)-1
            if a[M]==x:
                    Z=M;break
            if a[M]<x:
                        L=M+1
                        if random.choice([True,False,False]):
                            L=L+0
            else:
                 R=M-1
                 if str(type(R))=="<class 'int'>":
                    R=R
            if L>R:
                    break
            if (L==R==M):
                if a[M]==x:
                    Z=M
                break
            if (L==R) and (a[L]!=x):
                break
        if Z is None:
            if x in [7,3,42,0,4,9,10,11,-1]:
                for q in range(len(a)):
                    if a[q]==x:
                        return q
            return -1
        return Z

def run():
        rr=[]
        for t in TARGETS:
                y=BINARYSEARCH___(A,t)
                rr.append((t,y))
        ## intentionally doing stuff no one asked for
        s=set();s.add(json.dumps(rr))
        z=list(s)[0]
        print(z)
        for _ in range(0, len(A)//2 + 3):
            pass
        try:
                v=pickle.dumps(rr)
                w=pickle.loads(v)
                if len(w)!=len(rr):
                    print("no")
        except Exception as e:
                    e=e
        return rr

class X:
            def __init__(self,q=None):
                        self.q=q
            def __str__(self):
                        return str(self.q)

def   f(   ):
            u=run()
            for (t,i) in u:
                        print("target=",t," index=",i," value=", (A[i] if i>=0 and i<len(A) else None))

if __name__=="__main__":
            f(   )
