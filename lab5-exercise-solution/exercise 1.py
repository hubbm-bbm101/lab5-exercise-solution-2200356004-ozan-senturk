n = int(input("please enter a number N ="))
loopn = 0
sumof= 0
for y in range (1,n+1):
    if y%2!=0:
         sumof = y + sumof
print ("sum of odd numbers", sumof)
for x in range (1,n+1):
    if x%2==0:
        loopn= loopn +1
print ("average of even numbers", loopn+1)
        
              