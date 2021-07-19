#creating a tuple using ()
t = (1,2,3,5)

#printing elements of tuple
print(t[0])

#cannot update the value in tuple
#t[0]=98 does not work here. It is the major difference between list and tuple

t1 = () #empty tuple
print(t1)
#t2 = (1) #wrong syntax to declare tuple with one element
t2 = (1,) #tuple with one element
print(t2)

#tuple methods
print(t.count(1)) #returns number of 1s in tuple
print(t.index(3))
print(sum(t))
 

