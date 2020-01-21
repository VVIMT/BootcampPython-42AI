class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []
    def add(self, account):
        if isinstance(account, Account):
            self.account.append(account)
        else:
            print("Warning")
            return False
    def transfer(self, origin, dest, amount):
        if float(amount) < 0:
            return False
        for elem_src in self.account:
            if (origin == elem_src.id or origin == elem_src.name) and (amount <= elem_src.value):
                for elem_dst in self.account:
                    if (dest == elem_dst.id or dest == elem_dst.name):
                        elem_src.transfer(-1 * amount)
                        elem_dst.transfer(amount)
                        return True
        return False


        """
            @origin: int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return         True if success, False if an error occured
"""

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
"""
        pass
