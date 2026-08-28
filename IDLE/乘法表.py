i=1
j=1
while i<10 and j<10:
 print(i,"*",j,"=",i*j,end="  ")
 if i==j:
  print()
  j=1
  i+=1
  continue
 j+=1
 
 
