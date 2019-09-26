class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    # def greet(self, other_person):
    #     print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def contact(self, email, phone):
        print("{}\'s email is {} and phone number is {}".format(self.name, self.email, self.phone))

# #1
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# #2
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
# #3
# sonny.greet(jordan)
# #4
# jordan.greet(sonny)
#5
sonny.contact(name, email, phone)
#6
