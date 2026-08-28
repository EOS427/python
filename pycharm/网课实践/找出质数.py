r1=range(1,11)
r2=range(2,11)
for it1 in r1:
    for it2 in r2:
       if it1==it2:continue
       elif it1%it2==0:
           print(f"{it1}",end=" ")
           break