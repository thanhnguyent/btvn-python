import json
class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    @classmethod
    def lis_acc(cls,fileJson):
        with open(fileJson, "r") as fin:
            data = json.load(fin)
        acc=[]
        for d in data:
            acc.append(cls(**d))
        return acc


list_Account= BankAccount.lis_acc("bank_accounts.json")
print(f"| {'Number':9} | {'Account Name':15} | {'Balance':15} |")
print(f"|{'-' * 11}|{ '-' * 17 }|{'-' * 17}|")
for ac in list_Account:
    print(f"| {ac.account_number:9} | {ac.account_name:15} | {ac.balance:15} |")