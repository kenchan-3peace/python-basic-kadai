import random

#varの値に指定がないのでとりあえず1000までの乱数で確認
var = random.randint(0,1000)

#一応varを表示
print(f"varの値は{var}")

#3で割れるか
check1 = var % 3
#5で割れるか
check2 = var % 5

if check1 == 0 and check2 == 0:
  print("FizzBuzz")
elif check1 == 0:
  print("Fizz")
elif check2 == 0:
  print('Buzz')
else:
  print(var)