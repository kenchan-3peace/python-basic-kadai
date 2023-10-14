class Human():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def printinfo(self):
    print(self.name)
    print(self.age)

user = Human("太郎", 40,)
user.printinfo()