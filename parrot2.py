class parrot:
    # instance attributes
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # instance method
    def sing(self,song):
         return "{} sings {}".format(self.name, song)
    def dance(self):
        return "{} is now dancing".format(self.name)
# insanciate the object
blu = parrot("blu", 10)


print(blu.sing("Happy"))
print(blu.dance())