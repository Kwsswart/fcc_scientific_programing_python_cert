class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []
    self.balance = 0.00

  def deposit(self, amount, description=""):
    self.balance += amount
    self.ledger.append({'amount': amount, 'description': description})
  
  def withdraw(self, amount, description=""):
    if not self.check_funds(amount):
      return False
    else: 
      self.balance -= amount
      self.ledger.append({'amount': -abs(amount), 'description': description})
      return True

  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    if self.withdraw(amount, f"Transfer to {category.category}"):
      category.deposit(amount, f"Transfer from {self.category}")
      return True
    return False
  
  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True
  
  def __repr__(self):
    header = ''.join([''.join(["*" for i in range(int((30-len(self.category))/2))]), self.category, ''.join(["*" for i in range(int((30-len(self.category))/2))])])
    details = []
    for entry in self.ledger:
      description = entry['description'][:23]
      amount = str(entry['amount'])[:7]
      if "." not in amount:
        amount+=".00"
      spaces = ''
      if len(description) + len(amount) != 30:
        for i in range(30-len(description)-len(amount)):
          spaces += " "
      details.append(description+spaces+amount)
    details = "\n".join(details)
    total = sum([entry["amount"] for entry in self.ledger])
    total = "Total: " + str(total)
    return "\n".join([header,details,total])

  def get_expenses(self):
    return sum(map(float, [-entry['amount'] for entry in self.ledger if entry['amount']<0]))
    
    


def create_spend_chart(categories):
  output = "Percentage spent by category\n"

  # Retrieve total expense of each category
  total      = 0
  expenses   = []
  labels     = []
  len_labels = 0

  for category in categories:
    expense    = sum(map(float,[-x['amount'] for x in category.ledger if x['amount'] < 0]))
    total     += expense

    if len(category.category) > len_labels:
      len_labels = len(category.category)

    expenses.append(expense)
    labels.append(category.category)

  # Convert to percent + pad labels
  for x in expenses:
    try: 
      x = (x/total)*100
    except:
      x = 0
  labels   = [label.ljust(len_labels, " ") for label in labels]

  # Format output
  for c in range(100,-1,-10):
    output += str(c).rjust(3, " ") + '|'
    for x in expenses:
      output += " o " if x >= c else "   "
    output += " \n"

  # Add each category name
  output += "    " + "---"*len(labels) + "-\n"

  for i in range(len_labels):
    output += "    "
    for label in labels:
      output += " " + label[i] + " "
    output += " \n"

  return output.strip("\n")