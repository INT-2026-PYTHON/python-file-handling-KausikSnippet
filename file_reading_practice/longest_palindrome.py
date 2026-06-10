"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""

filename = input("Enter file name: ")

longest = []
max_length = 0

with open(filename, "r") as file:
    for word in file:
        word = word.strip().lower()

        # Check if palindrome
        if word == word[::-1]:

            if len(word) > max_length:
                max_length = len(word)
                longest = [word]

            elif len(word) == max_length:
                longest.append(word)

print("Longest palindrome length:", max_length)

for word in longest:
    print(word)
    