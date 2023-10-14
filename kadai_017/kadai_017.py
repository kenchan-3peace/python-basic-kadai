class Human():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def check_adult(self):
    if self.age >= 20:
        print(f"{self.name}さんは、年齢{self.age}歳で20歳以上となりますので大人です")
    else:
         print(f"{self.name}さんは、年齢{self.age}歳で20歳未満となりますので大人ではありません")

users = [Human("太郎", 40,), Human("二郎", 30,), Human("三郎", 20,), Human("四郎", 10,), Human("五郎", 5,)]

for user in users:
    user.check_adult()

