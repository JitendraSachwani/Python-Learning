dict1 = { #keys:values
    "fast" : "in a quick manner",
    "tanisha" : "soc validation engineer",
    "marks" : [1,2,3,4], 
    "anotherdict" : {"tanisha" : "dancer"}
}

print(list(dict1.keys())) #print keys of the dictionary
print(dict1.values()) #prints values
print(dict1.items())  #prints the (key,value) for all contents of the dictionary
print(dict1)
updateDict = {
    "Lovish" : "Friend",
    "night" : "stars"
}
dict1.update(updateDict) #updates the dictionary by adding key,values from the updateDict
#it also updates already existing values
print(dict1)

print(dict1.get("tanisha")) #if tanisha1 is given here then it won't throw error nut it returns none 
#print(dict1["tanisha1"]) -----throws error as tanisha1 is not present in dict1
#python dictionary methods for more methods



