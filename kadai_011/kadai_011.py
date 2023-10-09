list = ["水","金","地","火","木","土","天","海","冥"]

print("for文の場合")
for i in list:
  print(i)

print("while文の場合")
index = 0
len_list = len(list)
while index < len_list:
  print(list[index])
  index = index + 1