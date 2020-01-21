from the_bank import Account, Bank

bank = Bank()
one = Account("one")
src = Account("vv")
two = Account("two")
dst = Account("ww")
three = Account("three")

src.value = 500.0
dst.value = 20.0

bank.add(one)
bank.add(src)
bank.add(two)
bank.add(dst)
bank.add(three)

print(hasattr(src, 'value'))
print(hasattr(dst, 'value'))
print("\n\n")

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