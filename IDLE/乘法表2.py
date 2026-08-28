i=1
j=1
while i<=9 and j<=9:
 print(i,"*",j,"=",i*j,end="  ")
 if i==j:
  print()
  i=1
  j+=1
  continue
 i+=1
