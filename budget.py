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

  def get_withdrawals(self):
    """returns sum of all withdrawals"""
    w = 0
    for l in self.ledger:
      if l['amount']<0:
        w += -l['amount']
    return w

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
      # docs.python.org/2/library/string.html#format-examples
      list += '{:<23}'.format(l['description'])[:23]
      t = '{:.2f}'.format(l['amount'])
      # maybe: display '#######' if amount is too long
      t = '{:>7}'.format(t)[:7]
      list += t + br 
    total = 'Total: ' + str(self.get_balance())
    return title + list + total

def create_spend_chart(categories):
  """return a string that is a bar chart"""
  br = '\n'
  title = 'Percentage spent by category' + br

  data = {}   # sums per category
  sum = 0     # sum over all categories
  longest = 0 # longest category name
  for category in categories:
    if not category.name in data:
      data[category.name] = 0
    w = category.get_withdrawals()
    data[category.name] += w
    if len(category.name)>longest:
      longest = len(category.name)
    sum += w

  perc = {} # percentage per category
  tuples = data.items() # dictionary -> list of tuples
  for k,v in tuples:
    perc[k] = int(v/sum * 10) * 10 # 75,4 -> 70

  list = ''
  for lp in range(100,-10,-10):
    list += "{:>3}".format(str(lp))+'| '
    for k,v in perc.items():
      if lp<=v:
        list += 'o  '
      else:
        list += '   '
    list += br
  
  sep = ('    {:->'+str(4+2*len(categories))+'}').format('') + br

  legend = ''
  for i in range(longest):
    legend += '   '
    for category in categories:
      if i<len(category.name):
        legend += '  '+category.name[i]
      else:
        legend += '   '
    legend += '  ' + br

  # remove br and add 2 extra spaces
  return title + list + sep + legend.rstrip() + '  '
