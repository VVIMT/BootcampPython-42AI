from the_bank import Account, Bank

bank = Bank()
src = Account("vv")
dst = Account("ww")

src.value = 500.0
dst.value = 20.0

bank.add(src)
bank.add(dst)

print("vv: ")
print(src.value)
print("\n")
print("ww: ")
print(dst.value)
print("\n")

bank.transfer(src.id, dst.id, 400.00)

print("vv: ")
print(src.value)
print("\n")
print("ww: ")
print(dst.value)
print("\n")

print(dir())