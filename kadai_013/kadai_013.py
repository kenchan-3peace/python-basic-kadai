purchase_amount = int(input("購入金額を入力してください"))
tax = 0.1

def payment(purchase_amount, tax):
  return purchase_amount + purchase_amount * tax

print(f"支払い金額は{payment(purchase_amount, tax)}円です")