TEXTS = '''Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.! 

At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick. 

The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''

users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

line = 45 * '-'

#1.
name = input('Enter your name: ')
password = input('Password: ')
print(line)

# 2.& 3.
if users.get(name) != password:
    print('Sorry, your login failed, try it again')
    print(line)
    quit()

else:
    print('Wellcome to the app,', name.upper(), '\nWe have 3 texts to be analyzed !')

print(line)

#4
for texty in TEXTS:
    texty = TEXTS.split("\n\n")
    listy_textu = [texty[0], texty[1], texty[2]]

user_selection = input('Please enter number of selected text: ')
print(line)

if user_selection.isalpha():
    print('Please enter only number from 1 to 3! Try again.')
    quit()

elif int(user_selection) > 3:
    print('Please enter only number from 1 to 3! Try again.')
    quit()

else:
    selected_text = listy_textu[int(user_selection) - 1]


#5
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for element in selected_text:
  if element in punctuation:
    selected_text = selected_text.replace(element, '')

single_word = selected_text.split()

for word in single_word:
  clean_word = word.strip(',.!')

nr_word = len(selected_text.split())
print(f'There are {nr_word} words in the selected text')

title_word = []
upper_word = []
lower_word = []
numeric_word = []
total_sum = []

for word in single_word:
  if str(word).istitle():
    title_word.append(word)
  if str(word).isupper() and (len(str(word))) > 2:
    upper_word.append(word)
  elif str(word).islower():
    lower_word.append(word)
  elif str(word).isnumeric():
    numeric_word.append(word)
print(f'There are {len(title_word)} titlecase words.')
print(f'There are {len(upper_word)} uppercase words.')
print(f'There are {len(lower_word)} lowercase words.')
print(f'There are {len(numeric_word)} numeric strings.')

for i in numeric_word:
  total_sum.append(int(i))
print(f'The sum of all the numbers is {sum(total_sum)}.')
print(line)

#6
vycisteno = [word.strip(',.!') for word in single_word]

print('LEN | OCCURENCES | NR')
print(line)

word_length = {}
for clean_word in vycisteno:
  clean_word = len(clean_word)
  word_length[clean_word] = word_length.setdefault((clean_word), 0) + 1


for item, char in sorted(word_length.items(), key=lambda wl:(wl[0])):
  print(item   ,char * '*' ,  char)