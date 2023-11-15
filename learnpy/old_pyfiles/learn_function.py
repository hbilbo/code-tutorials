print("----Functions----")
sentence = "George and Jerry meet at the coffee shop with Kramer"
words = ['Bill','Jimmy','Steven']
def replace_word(s,names):
    s = s.replace("George",names[0])
    s = s.replace("Jerry",names[1])
    s = s.replace("Kramer",names[2])
    return s

output = replace_word(sentence,words)
print(output)

# Define a function with a default input value. Use docstrings to describe function.
import random
def dna(length=20):
    """
    Creates a strand of DNA

    Arguments
     - Length: int

    Returns: str
    """
    return "".join(random.choices("ATGC",k=length))

DNA = dna(30); print(DNA)
def rna(dna):
    return dna.replace("T","U")
RNA = rna(DNA); print(RNA)

#Lambda function - single line function, can be stored as an object
print("\n----Lambda Functions----")
songs = ["1.mp3","2.flac","3.mp3","4.mp3"]

filter_mask = lambda song: song.endswith(".mp3")
print(filter_mask)

#Filter method - can filter out a specific file type
print("\n----Filter Method----")
filt_songs = list(filter(filter_mask,songs))
print(filt_songs)

#This is quivalent to the labmda function
def filter_mask_func(s):
    return s.endswith(".mp3")

filt_songs2 = list(filter(filter_mask_func,songs))
print(filt_songs2)
print(type(filter_mask)); print(type(filter_mask_func))

#Map method
print("\n----Map Method----")
song = "1.mp3"
#rename to my_song_1.flac
song_rn = lambda song: f"my_song_{song.split('.')[0]}.flac"
print(song_rn(song))
#can use map to apply this renaming to a list of variables similar to filter
new_songs = map(song_rn,songs)
print(list(new_songs))

#Reduce method
print("\n----Reduce Method----")
from functools import reduce
numbers = [1,2,3,4,5]
numbers_sum = reduce(lambda result,value: result + value,numbers)
print(numbers_sum)
#can use "sum" method to do the same thing
print(sum(numbers))

#*args and **kwargs
print("\n----*args and **kwargs----")
def test(my_arg,*args,**kwargs):
    print(my_arg)
    print(args)
    print(kwargs)

test(1, 2, 3, "a", "d", var1="h", var2=8)

#Challenge - reverse DNA strand and make these substitutions:
#A->T,C->G,G->C,T->A
print("\n----Challenge----")
chal_dna = dna(10)
print(chal_dna)
# help("".join)
rev_dna = "".join(list(reversed(chal_dna)))
# print(rev_dna)
new_dna = rev_dna.replace('A','t').replace('C','g').replace('G','c').replace('T','a').upper()
print(new_dna)
#Alternative method
print('--Alt Method--')
def make_trans(strand):
    translation_table = str.maketrans("ACGT","TGCA")
    strand = strand.translate(translation_table)
    strand = strand[::-1]
    return strand
new_dna2 = make_trans(chal_dna)
print(new_dna2)
print('complimentary pair:\n ',list(zip(chal_dna,new_dna2)))