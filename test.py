class Account:
    def __init__(self, account_id: str, balance: float):
        self.account_id: str = account_id
        self.balance: float = balance
    
    def deposit(self, amount: float):
        self.balance += amount
    
    def get_balance(self):
        return self.balance

class Bank:
    
    def __init__(self):
        self.accounts: dict[str, Account] = {}
        
    def create_account(self, account_id: str):
        for key, value in self.accounts.items():
            if account_id not in self.accounts:
                account = Account(account_id, 0)
                self.accounts.update({account_id: account})
            else:
                print("Account with this ID already exists")
    
    def deposit(self, account_id: str, amount: float):
        for key, value in self.accounts.items():
            if value.account_id == account_id:
                 value.balance += amount
        
        
    def get_balance(self, account_id: str):
        for key, value in self.accounts.items():
            if key == account_id:
                return value
            
bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())



#def create_account(self, account_id: str):
  #      account = Account(account_id, 0)
 #       self.accounts.update({account_id: account})
   #     return account






class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def symmetric(tree: list[int]) -> bool:
    # scrivere qui la vostra funzione
    flag: bool = True
    i: int = tree[0]
    while i in range(len(tree)):
        if 2*i+1 != None and 2(i+1) != None:
            flag = True
            i += 1
        elif 2*i+1 == None and 2(i+1) == None:
            flag = True
            i += 1
        else:
            flag = False
    return flag   



class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def is_symmetric(self):
        flag = True
        if left and right:
            flag = True
        elif not left and not right:
            flag = True
        else:
            flag = False
        return flag
        
def symmetric(tree: list[int]) -> bool:
    # scrivere qui la vostra funzione
    for i in range(len(tree)):
        node = TreeNode(tree[i], tree[i+1], tree[i+2])
        node.is_symmetric(node)