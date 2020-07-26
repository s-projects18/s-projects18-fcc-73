import replit
replit.clear()

class Category:
  """objects based on different budget categories"""
  # static/ Class scope
  # myStatic=42

  def __init__(self, category):
    self.name = category
    self.ledger = [] # instance scope

  def deposit(self, amount, description=''):
    """append an object to the ledger list"""
    self.ledger.append({'amount':amount, 'description':description})

  def withdraw (self, amount, description=''):
    """the amount should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger"""
    if self.check_funds(amount):
      self.ledger.append({'amount':-amount, 'description':description})
      return True
    return False

  def get_balance(self):
    """returns the current balance of the budget category"""
    balance = 0
    for l in self.ledger:
      balance += l['amount']
    return balance

  def transfer(self, amount, categoryObject):
    """add a withdrawal with the amount and the description 'Transfer to [Destination Budget Category]'"""
    if self.withdraw(amount, "Transfer to "+categoryObject.name):
      categoryObject.deposit(amount, "Transfer from "+self.name)
      return True
    return False

  def check_funds(self, amount):
    """returns True if the amount is less/equal than the balance of the budget category and returns False otherwise"""
    funds = 0 # local scope
    for l in self.ledger:
      funds += l['amount']
    if amount>funds:
      return False
    return True

  def __str__(self): # like: toString()
    """returns formatted: title, list, total"""
    br = '\n'
    title = self.name.center(30, '*') + br
    list = ''
    for l in self.ledger:
      #t = l['description'].ljust(23, ' ')
      list += '{:<23}'.format(l['description'])[:23]
      t = '{:.2f}'.format(l['amount'])
      t = '{:>7}'.format(t)
      list += t + br 
    total = 'Total: ' + str(self.get_balance())
    return title + list + total

def create_spend_chart(categories):
  """return a string that is a bar chart"""
  pass

c = Category("foo42")
c.deposit(888)
c.withdraw(40)
print(c)