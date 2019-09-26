from pprint import pprint
from characters import characters

#For each of these questions, write a function that returns the answer.

#1 How many characters names start with "A"?

# def how_many_a():
#     count = 0
#     for character in characters:
#         if character['name'].startswith('A'):
#             # pprint(character['name'])
#             count += 1 
#     print(count)
# how_many_a()


#3 How many characters names start with "Z"?

# def how_many_z():
#     count = 0
#     for character in characters:
#         if character['name'].startswith('Z'):
#             # pprint(character['name'])
#             count += 1 
#     print(count)
# how_many_z()

#4 How many characters are dead?
# def are_dead():
#     count = 0
#     for character in characters:
#         if character['died'] != '':
#             count += 1
#     print(count)
# are_dead()


#5 Who has the most titles?
# most_titles = [ ]
# def has_title():
#     for character in characters:
#         if len(character['titles']) > 1:
#             most_titles.append(character['name'])
#             # most_titles.append(str(character['titles']))
#             # print(character['name'], len(character['titles']))
#             # most_titles = [character['name'] + str(len(character['titles']))]

# has_title()
# print(str(max(most_titles)) + " " + str(len(characters[1]['titles'])))
# #not right person

#Sean's way
most_titles = 0
for person in characters:
        num_titles = len(person['titles'])
        if num_titles > most_titles:
        most_titles = num_titles

for person in characters:
num_titles = len(person['titles'])
        if num_titles == most_titles:
        print("%s has %d titles" % (person['name'], most_titles))


#6 How many are Valyrian?



#7 What actor plays "Hot Pie" (and don't use IMDB)?



#8 How many characters are *not* in the tv show?



#9 Produce a list characters with the last name "Targaryen"



#10 Create a histogram of the houses (it's the "allegiances" key)       