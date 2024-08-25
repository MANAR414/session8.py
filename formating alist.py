n=int(input("enter no. of element:"))
elmt=[]
for i in range(n):
   e=input()
   elmt.append(e)
if n==1:
   print(elmt[0])
elif n==2:
   print(elmt[0],"and",elmt[1])
elif n==3:
   print(elmt[0],",",elmt[1],"and",elmt[2])
elif n>3:
   r=",".join(elmt[0:3])
   j=' and '.join([elmt[-2],elmt[-1]])
   print(r,",",j)























