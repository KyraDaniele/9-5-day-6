class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def contact(self):
        return("{}\'s email is {} and phone number is {}".format(self.name, self.email, self.phone))
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

#5
print(sonny.contact())
print(jordan.contact())