animal_1 = "dog"
animal_2 = "monkey"
animal_3 = "zebra"
#Concatenation
print(animal_1 + animal_2 + animal_3)
#Lists
animals = [animal_1, animal_2, animal_3]
print(animals)
numbers = [1,2,3,4]
print(type(numbers))
numbers2 = range(1,10)
print(numbers2[2:3])
#Indexing
print("----Indexing----")
print(numbers[0]) #first value
print(numbers[-1]) #index last value
print(numbers[2:]) #remove first two values
numbers += [5]; print(numbers)
#Referencing
print("----Referencing----")
vec1 = [0,4,6,8]
vec2 = vec1
vec3 = vec1.copy()
vec2.append(9) #vec1 also appends 9 since they are referenced together. need to use "copy" to separate them
print(vec1)
print(vec3)
#Methods
print("----Methods----")
vec3.append([2,3,4]) #append imbeds this as another list
print(vec3)
vec3.extend([2,3,4]) #extend imbeds the numbers themselves into the list
print(vec3)

#Dictionaries - Contain key-value pairs
print("----Dictionaries----")
vocab = {
    #key: value
    "hola": "hello",
    "bueno": "good"
}
print(vocab)
print(vocab["hola"])
vocab["dormir"] = "to sleep"
print(vocab["dormir"])
vocab[1] = "test"; print (vocab)
# print(dir(vocab))
#Sets - remove duplicate items and can be used to see differences
print("----Sets----")
a1 = [1,3,6,2,5,2]
a2 = [1,7,6,5,3,6]
s1 = set(a1); print("s1 = ",s1)
s2 = set(a2); print("s2 = ",s2)
s3 = s1 - s2; print("s1 - s2 = ",s3)
#Tuples - these are lists that cannot be changed, only read
print("----Tuples----")
color = (255, 0, 0)
red, green, blue = color
print(red, green, blue)
