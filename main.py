#This is the main python page

# In this program we will take several inputs from a user and provide information about what those words are, their composition, and their properties.

#this input takes a name, color, and a  pet name.
#These inputs will later be used to get information about them. 
name = input("Please enter your name: ")
color = input("Please enter a color: ")
pet = input("Please enter the name of a pet: ")
  
#strings to check if a characters is a vowel or consonant
vowels = "aeuio"
consonants = "qwrtyplkjhgfdszxcvbnm"

try:
  #Prints an output of what the users color is
  print("Your name is ", name, ", your color is ", color, ", and the pet name you gave is ", pet)

  #Convert the input strings to lowercase to better gain information about them.
  name = name.lower()
  color = color.lower()
  pet = pet.lower()

  nameVowels = 0
  nameConsonants = 0
  for character in name:
    if character in vowels:
      nameVowels += 1
    elif character in consonants:
      nameConsonants += 1
  print ("Length of name: ", len(name))
  print ("Your name has ", nameVowels, " vowels and ", nameConsonants, "consonants.")

  colorVowels = 0
  colorConsonants = 0
  for character in color:
    if character in vowels:
      colorVowels += 1
    elif character in consonants:
      colorConsonants += 1
  print ("Length of color: ", len(color))
  print ("Your color has ", colorVowels, " vowels and ", colorConsonants, "consonants.")

  petVowels = 0
  petConsonants = 0
  for character in pet:
    if character in vowels:
      petVowels += 1
    elif character in consonants:
      petConsonants += 1
  print ("Length of pet name: ", len(pet))
  print ("Your pet name has ", petVowels, " vowels and ", petConsonants, "consonants.")
except: 
  print ("Invalid Input")
