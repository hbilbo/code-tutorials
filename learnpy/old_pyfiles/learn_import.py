from math import sqrt
#math is the module, sqrt is the function
a = sqrt(9); print(a)
import itertools as itools
#import a module under a different name
A = [1,2,3]
B = [4,5,6]
C = [7,8,9]
D = itools.product(A,repeat=3)
E = itools.product(A,B,C)
print(list(D),f"\n\n{list(E)}")
import time
time.sleep(1) #sleep for one second

import random
activities = ["run","swim","jump","climb"]
weights = [5,1,10,3]
rdm = random.choices(activities,weights,k=8)
print(f"\n{rdm}")

from collections import Counter
code = ['up','up','down','down','left','right','left','right','B','A','start']
count = Counter(code)
print(count); print(type(count))
lft = count["left"]; print(lft)
print(count.total())

import faker
# print(dir(faker))
fake = faker.Faker()
eml = fake.email()
pss = fake.password()
print(f"\n{eml}"); print(pss)
# print(dir(fake))

import pandas as pd
df = pd.DataFrame({
    "a": 1,
    "b": pd.Timestamp('20230609'),
    "c": pd.Series([1,2,3,4],dtype='float32'),
    "d": pd.Categorical(["Test","Train","Test","Train"]),
    "e": "foo"
})
print(df)