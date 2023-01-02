#this is a script that will prompt the user for a word and search a text file which contains a speech
#it will find the number of occurances of this word and print its findings
#personally, I would use this if I am practicing for a presentation and want to find the number of times I say "um" or "like" in order to improve my presentation skills
#also has a script to find phone numbers through a regular expression and the re module just for fun
#if you wanted to figure out if there was any contact information in a long document this would also be useful

#firstly import re module
import re

#speech.txt document that we are using to test is George Washington's farewell address with an added number at the end to test
#you can put any text file in place of speech.txt to test your own speech
# need to open the file read it then close the file and put the read contents into speech 
file = open("speech.txt", "r") #r because we are going to read the file
speech = file.read()
file.close()
#could just use .count(word) to find the word in a string but we are using .split
#we are putting each word at each index in an array so that when we for i in str it won't go through each character
#but rather each word
speech = speech.lower() #will make all words lowercase so capatilization does not matter
arspeech = speech.split(" ")

word = input("Enter the word that you would like to check for (enter a string in parenthesis): ")
#likec and umc are the counts to count how many time I say like or um
wordc = 0

for i in arspeech:
    if i == word:
        wordc += 1

#can't do + int with a str so need to convert variables to strings to add them
print("Number of times "+ str(word)+ " was said: "+ str(wordc))

#Regex practice*
#will identify if a number is said or not just for practice of regex and fun, in python ^ at beginning and $ at end not needed ig
# ########## and ###-###-#### numbers accepted, if not either of those formats then not accepted as a valid number, also only zero to one '-' at a time so we need '?'
pattern = '([0-9]{3}(\-)?){2}[0-9]{4}'
#re is a regular expression operation module that provides operations
foundNum = re.search(pattern, speech)

if foundNum:
    print("A number was found in the speech.")
else:
    print("No number in speech.")
