#import primefac
#list(primefac.primefac(44))

import math
from timeit import default_timer as timer

from SqM import squaremultiply



#-----------------------------------------------------------------------------


p=9993451781

g=3

pk = 3424750084

#----------------------------------------------------------------------------

print("---------Brute Force Attack--------------")

#Brute force

z=1
x=0
start = timer()
flag = True
while flag:
    x=x+1
    z=(z*g)%p
    if z==pk:
        flag = False
end = timer()
mm = (end - start)/60
#print the total time employed to check all keys
print(mm ,"minutes") # Time in minutes.
print(math.log(x,2), "log_2(iterations)" )
print("secret key = ", x)
