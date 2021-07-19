a = {1,3,4,5, 1} #----set
print(a)
print(type(a))
#sets don't print repetitve items

#a = {} -----it is empty dictionary and not set

#syntax for empy set
b = set()
print(type(b))

#methods for set
b.add(4)
b.add(5)
#b.add([1,2,3]) ----list cannot be added as sets can't be changed but list can 
#similarily with dictionary type
b.add((1,2,3)) #---a tuple can be added as both cant be changed
print(b)

print(len(b))
#b.remove(5) ---removes 5 from set
print(b.pop()) #----removes any random element
print(b)
#b.clear()-----clears the set
#b.union()
#b.intersection()

