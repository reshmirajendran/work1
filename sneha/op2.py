# class person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# x = Person("John", "Doe")
# x.printname()

class dog:
    def pet(self):
        print("iam a pet")
class animal(dog):
          def anime(self):
                super().pet()
                print("iam a dog")
ob=animal()
ob.anime()
                