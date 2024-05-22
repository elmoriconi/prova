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
        
"""def symmetric(tree: list[int]) -> bool:
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
    return flag"""   


def symmetric(tree: list[int]) -> bool:
    return are_mirrored(tree, 1, 2)

def are_mirrored(tree: list[int], left_index: int, right_index: int):
    if left_index >= len(tree) or right_index >= len(tree):
        return left_index == right_index
    if tree[left_index] != tree[right_index]:
        return False
    left_of_left = 2*left_index + 1
    right_of_left = 2* (left_index + 1)
    left_of_right = 2*right_index + 1
    right_of_right = 2* (right_index + 1)
    symmetric_extremes = are_mirrored(tree, left_of_left, right_of_right)
    symmetric_inner = are_mirrored(tree, right_of_left, left_of_right)
    return symmetric_extremes and symmetric_inner

#no è tutto sbagliato non hai capito la consegna
class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def is_symmetric(self):
        flag = True
        if self.left and self.right:
            flag = True
        elif not self.left and not self.right:
            flag = True
        else:
            flag = False
        return flag
        
def symmetric(tree: list[int]) -> bool:
    # scrivere qui la vostra funzione
    for i in range(len(tree)):
        node = TreeNode(tree[i], tree[2*i+1], tree[2*(i+1)])
        node.is_symmetric(node)