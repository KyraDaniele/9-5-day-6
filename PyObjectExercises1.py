# #1. Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
# Have sonny greet jordan using the greet method.
# Have jordan greet sonny using the greet method.
# Write a print statement to print the contact info (email and phone) of Sonny.
# Write another print statement to print the contact info of Jordan.

class Person:
    def __init__(self, name, email, phone, friends):
        self.name = name
        self.email = email
        self.phone = phone
        # def __init__(self, friends):
        self.friends = []

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def contact(self):
        return("{}\'s email is {} and phone number is {}".format(self.name, self.email, self.phone))

    def print_contact_info(self):
        return('{}\'s email: {}, {}\'s phone number: {}'.format(self.name, self.email, self.name, self.phone))

    def add_friend(self, new_friend: 'Person'):
        self.friends.append(new_friend)
    def num_friends(self, friends):
        return('{} has {} friend(s).'.format(self.name, len(self.friends)))


# #1
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948", [])
# #2
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456", [])
# #3
sonny.greet(jordan)
#4
jordan.greet(sonny)

print(sonny.print_contact_info())

print(jordan.add_friend(sonny))

print(jordan.num_friends('friends'))
# jordan.friends.append(sonny) 
# sonny.friends.append(jordan)

# print("Jordan has " + str(len(jordan.friends)) + " friend(s).")
