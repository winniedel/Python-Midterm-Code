# Midterm Exam
# Assigned on October 28. Due October 30, 11:59.
# You're allowed to use resource such as python.org, but you're not allowed
# to copy other people's code. Your work should be independent.
# Every question is 20 points.


# 1. Write a Python program to check whether an alphabetic character is a
#    vowel or consonant.
#    Expected Output:
#    Inut a letter of the alphabet: k
#    k is a consonant

word = input("Enter a word:")
if "a" and "A" in word or "e" and "E" in word or "i" and "I" in word or "o" and "O" in word or "u" and "U" in word:
   print("The vowels are",)
   
if "a" in word or "A" in word:
    print("a")
if "e" in word or "E" in word:
   print("e")
if "i" in word or "I" in word:
    print("i")
if "o" in word or "O" in word:
    print("o")
if "u" in word or "U" in word:
    print("u")

if "b" and "B" in word or "c" and "C" in word or "d" and "D" in word or "f" and "F" in word or "g" and "G" in word or "h" and "H" in word or "j" and "J" in word or "k" and "K" in word or "l" and "L" in word or "m" and "M" in word or "n" and "N" in word or "p" and "P" in word or "q" and "Q" in word or "r" and "R" in word or "s" and "S" in word or "t" and "T" in word or "v" and "V" in word or "w" and "W" in word or "x" and "X" in word or "y" and "Y" in word or "z" and "Z" in word:
    print("The consonants are",)
if "b" in word or "B" in word:
    print("b")
if "c" in word or "C" in word:
    print("c")
if "d" in word or "D" in word:
    print("d")
if "f" in word or "F" in word:
  print("f")
if "g" in word or "G" in word:
   print("g")
if "h" in word or "H" in word:
    print("h")
if "j" in word or "J" in word:
    print("j")
if "k" in word or "K" in word:
    print("k")
if "l" in word or "L" in word:
   print("l")
if "m" in word or "M" in word:
    print("m")
if "n" in word or "N" in word:
    print("n")
if "p" in word or "P" in word:
    print("p")
if "q" in word or "Q" in word:
   print("q")
if "r" in word or "R" in word:
    print("r")
if "s" in word or "S" in word:
   print("s")
if "t" in word or "T" in word:
    print("t")
if "v" in word or "V" in word:
   print("v")
if "w" in word or "W" in word:
    print("w")
if "x" in word or "X" in word:
    print("x")
if "y" in word or "Y" in word:
   print("y")
if "z" in word or "Z" in word:
    print("z")




# 2. Write a Python program to display the sign of the Chinese Zodiac for given
#    year in which you were born.


year = int(input("What year were you born?:"))

if year == 1996:
    zodiac = 'Rat'
    print("Year of the Rat!")
elif year == 1997:
    print("Year of the Ox!")
elif year == 1998:
    print("Year of the Tiger!")
elif year == 1999:
    print("Year of the Rabbit!")
elif year == 2000:
   print("Year of the Dragon!")
elif year == 2001:
    print("Year of the Snake!")
else:
   print("Information unknown")


## 3. Write a for loop that iterates over a list of strings lst
##    and prints the first three characters of every word.
##    If lst is the list ["Montclair","State", "University"],
##    then the following will be printed:
##    Mon
##    Sta
##    Uni

list = ["Montclair", "State", "University"]
for me in list:
   if len(me)>1:
       print(me[:3])



##  4. In order to understand what a program tries to accomplish, it is essential to be able to follow the flow
##     of control. In the following example, what happens when x = 4? 
while True:
     for x in range(6):
         y = 2*x+1
        print(y)
       if y>9:
             break

## (a) The program breaks out of the while loop and stops running
## (b) The program breaks out of the for loop, but the while condition continues to be True, resulting in an infinite
##     loop.
## (c) The program does not break, but simply continues processing the for loop.

#The answer is C


##  5.  Write a program that adds all the digits in an integer. If the resulting sum is more than one digit, keep repeating
##      until the sum is one digit. For example, 123456 has the sum 1+2+3+4+5+6 = 21 which has the sum of 2+1 = 3, your final answer.
##      use the input() function to prompt the user to enter a positive integer. Use while loop.


##I wasn't sure how to do this one

        
    


