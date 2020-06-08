
num = 407

if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"x",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       

else:
   print(num,"is not a prime number")