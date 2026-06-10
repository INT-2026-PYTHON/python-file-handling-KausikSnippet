"""
## 6. Words in sonnet_words.txt but NOT in sowpods.txt  *(Hard)*

=================================================
WORDS UNIQUE TO THE SONNET
=================================================

Problem Statement:
Read the text files `sowpods.txt` and
`sonnet_words.txt`. PRINT every word that
appears in `sonnet_words.txt` but does NOT
appear in `sowpods.txt`.

This problem is about CHOOSING THE RIGHT DATA
STRUCTURE. If you check each sonnet word
against the SOWPODS list with a nested loop,
the work is O(N*M). Using SETS turns the
membership check into O(1), giving you an
overall O(N + M) algorithm.

-------------------------------------------------
Input Example:
sowpods.txt sample:
   thee
   love
   summer
   day
   eyes
   shall
   more

sonnet_words.txt sample:
   shall
   i
   compare
   thee
   to
   a
   summer
   day

Output Example:
Words in sonnet but not in sowpods:
['a', 'compare', 'i', 'to']
Total: 4

-------------------------------------------------
Explanation:
sonnet words -> {'shall', 'i', 'compare',
                 'thee', 'to', 'a', 'summer',
                 'day'}
sowpods set   -> {'thee', 'love', 'summer',
                  'day', 'eyes', 'shall',
                  'more'}
Difference (sonnet - sowpods)
              -> {'i', 'compare', 'to', 'a'}
After sorting -> ['a', 'compare', 'i', 'to'].
=================================================

"""

filename1 = input("Enter sowpods file name: ")
filename2 = input("Enter sonnet file name: ")

# Step 1: Read sowpods into a set
sowpods_set = set()

with open(filename1, "r") as file:
    for line in file:
        word = line.strip().lower()
        sowpods_set.add(word)              #add each word to sowpods_set

# Step 2: Read sonnet words into another set
sonnet_set = set()

with open(filename2, "r") as file:
    for line in file:
        word = line.strip().lower()
        sonnet_set.add(word)               #add each word to sonnet_set

# Step 3: Find difference (words in sonnet but not in sowpods)
result = sorted(sonnet_set - sowpods_set)

# Step 4: Print output
print("Words in sonnet but not in sowpods:")
print(result)
print("Total:", len(result))

