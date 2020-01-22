from the_bank import Account, Bank

bank = Bank()
one = Account("one")
src = Account("vv")
two = Account("two")
dst = Account("ww")
three = Account("three")

src.value = 500.0
dst.value = 20.0

src.zip = []
dst.zip = []

src.addr = []
dst.addr = []

bank.add(one)
bank.add(src)
bank.add(two)
bank.add(dst)
bank.add(three)


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

print("__dict__ from src: \n")
print(dir(src))
print("\n")
print("__dict__ from dst: \n")
print(dir(dst))
print("\n")
print(len(dir(src)))
print("\n")
print(len(dir(dst)))
print("\n")

print("fix src: ")
bank.fix_account(src)
print("fix dst: ")
bank.fix_account(dst)

print("Fixed __dict__ from src: \n")
print(dir(src))
print("\n")
print("Fixed __dict__ from dst: \n")
print(dir(dst))
print("\n")
print(len(dir(src)))
print("\n")
print(len(dir(dst)))
print("\n")

print("fix src: ")
bank.fix_account(src)
print("fix dst: ")
bank.fix_account(dst)

print("Fixed_2 __dict__ from src: \n")
print(dir(src))
print("\n")
print("Fixed_2 __dict__ from dst: \n")
print(dir(dst))
print("\n")
print(len(dir(src)))
print("\n")
print(len(dir(dst)))
print("\n")
