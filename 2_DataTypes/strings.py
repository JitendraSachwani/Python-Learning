#string- sequence of characters

#string slicing:
name = "tanisha "
surname = "sharma"
print(type(name))
c = name + surname #concatenation
print(c)
print(name[0]) #indexing of string
print(name[0:3]) #prints 0,1,2.....excludes 3. This is called string slicing

#negative string indexing -  used to access the last index of the string in case we don't know the length of the string
#negative indices start from -1
print(name[:4])  #same as 0:4
print(name[1:])  #same as 1:7 where 7 is the length of the string is 0,1,2,3,4,5,6

#slicing with skip value
d = name[1:6:2]
e = name[0::2]
print(d)
print(e)




