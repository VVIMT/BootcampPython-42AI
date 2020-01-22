class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    #"""The bank"""
    def __init__(self):
        self.account = []
    def add(self, account):
        if isinstance(account, Account):
            self.account.append(account)
        else:
            print("Not an Account object")
            return False
    def transfer(self, origin, dest, amount):
        if float(amount) < 0:
            return False
        for elem_src in self.account:
            if (origin == elem_src.id or origin == elem_src.name) and (amount <= elem_src.value):

                print("src: ")
                print(elem_src.id)
                print("origin: ")
                print(origin)
                print("value: ")
                print(elem_src.value)
                print("amount: ")
                print(amount)
                print("\n")

                for elem_dst in self.account:

                    print(elem_dst)
                    print("\n")

                    if (dest == elem_dst.id or dest == elem_dst.name):
                        elem_src.transfer(-1 * amount)
                        elem_dst.transfer(amount)

                        print("src value: \n")
                        print(elem_src.value)
                        print("\n")
                        print("dst value: \n")
                        print(elem_dst.value)
                        print("\n")

                        return True
        return False


        #"""
        #    @origin: int(id) or str(name) of the first account
        #    @dest:    int(id) or str(name) of the destination account
        #    @amount: float(amount) amount to transfer
        #    @return         True if success, False if an error occured
        #"""
    
    def check_account(self, account):
        if not hasattr(account, 'id'):
            print("No attribute 'id'\n")
            return 1
        if not hasattr(account, 'name'):
            print("No attribute 'name'\n")
            return 2
        if not hasattr(account, 'value'):
            print("No attribute 'value'\n")
            return 3
        i = 0
        while i < len(dir(account)):
            if (dir(account)[i][:1]) == 'b':
                print("Attribute starting with 'b'\n")
                return 4
            i += 1
        i = 0
        while i < len(dir(account)):
            print(dir(account)[i][:3])
            if (dir(account)[i][:3]) == 'zip':
                break
            i += 1
            if i == len(dir(account)):
                print("No attribute starting with 'zip'\n")
                return 5
        i = 0
        while i < len(dir(account)):
            print(dir(account)[i][:4])
            if (dir(account)[i][:4]) == 'addr':
                break
            i += 1
            if i == len(dir(account)):
                print("No attribute starting with 'addr'\n")
                return 6
        if len(dir(account)) % 2 == 0:
            print("Even number of attributes\n")
            return 7
        return 0

    def fix_account(self, account):
        try:
            check = self.check_account(account)
            if check == 1:
                account.id = Account.ID_COUNT + 1
            if check == 2:
                account.name = "_" + str(account.id) + "_"
                while account.name in self.account:
                    account.name += str(account.id)
        except Exception:
            print("An error occured")
            return False

        return True
        #"""
        #fix the corrupted account
        #@account: int(id) or str(name) of the account
        #@return         True if success, False if an error occured
        #"""

