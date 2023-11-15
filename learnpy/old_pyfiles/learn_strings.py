str1 = "This is a Sentence"
print(str1)
print(str1.upper())
tp = type(str1)
#f string
print(f"class: {tp}")
print("class:",tp)
# print(dir(str1))

c = str1.count; print("\n",c)
c1 = "hi" in "hello"; print(c1)
c2 = "rat" in "scratch"; print(c2)

str2 = "I've got to get a new phone, mine keeps dying!"
print(str2)
# """" Inefficient method of removing the comma
str3 = str2.split(",")
str3_1 = str3[0] + str3[1]
str3_2 = ''.join(str3)
print(str3_1)
print(str3_2)
# """
str4 = str2.lower().replace(",","").replace("'","").replace("!","")
print(str4,'\n')

#EXAMPLE
s = "this is my string"
s_sp = s.split(maxsplit=2)
print(s_sp,'\n')

##These use topics from learn_collections,learn_num,learn_loops
#EXAMPLE - Convert string array to formatted list of lists
input_data = """Name,Phone,Address
Mike Smith,15554218841,123 Nice St, Roy, NM, USA
Anita Hernandez,15557789941,425 Sunny St, New York, NY, USA
Guido van Rossum,315558730,Science Park 123, 1098 XG Amsterdam, NL"""
print(input_data)
customers = input_data.split('\n')[1:] #generates list of separate lines
format1 = [inp.split(',',maxsplit=2) for inp in customers]
print(format1,'\n')
#Alternatively
results = []
for line in input_data.split('\n')[1:]:
    results.append(line.split(',', maxsplit=2))

#EXAMPLE - Convert list of lists to single string
weather = [
    ['Boston', 'MA', '76F', '65% Precip', '0.15 in'],
    ['San Francisco', 'CA', '62F', '20% Precip', '0.00 in'],
    ['Washington', 'DC', '82F', '80% Precip', '0.19 in'],
    ['Miami', 'FL', '79F', '50% Precip', '0.70 in']
]
weather1 = []
for list in weather:
    weather1.append(','.join(list))
weather1 = '\n'.join(weather1)
print(weather1,'\n')
# Alternatively leveraging list comprehension
weather2 = [','.join(row) for row in weather]
weather2 = '\n'.join(weather2)
print(weather2)