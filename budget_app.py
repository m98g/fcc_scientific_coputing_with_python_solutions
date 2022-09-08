class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
   # up here was not the problem, the self refrencing down below in transfer was the problem
    total_amount = '%.2f' % self.get_balance()
    total = "Total: " + str(total_amount)
    
    other_lines = []
    other_lines.append("*" * int((30 - len(self.name))  / 2) + self.name + "*" * int((30 - len(self.name))  / 2))
    for i in self.ledger:
      if len(i["description"]) > 23:
        description = i["description"][:23]
        amount1 = '%.2f' % i["amount"]
        amount = str(amount1).rjust(7)
        line = description + amount
        other_lines.append(line)

      else:
        description = str(i["description"]).ljust(23)
        amount1 = '%.2f' % i["amount"]
        amount = str(amount1).rjust(7)
        line = description + amount
        other_lines.append(line)

    other_lines.append(total)
    return("\n".join(other_lines))

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})
    
  def withdraw(self, amount, description = ""):
    flag = self.check_funds(amount)
    if flag:
      self.ledger.append({"amount": -abs(amount), "description": description})

    return(flag)
    
  def get_balance(self):
    funds = sum([i["amount"] for i in self.ledger])
    return(funds)
    
  def transfer(self, amount, other_category):
    flag = self.check_funds(amount)
    if flag:
      other_category.deposit(amount, description = f"Transfer from {self.name}")
      self.withdraw(amount, description = f"Transfer to {other_category.name}")    
    return(flag)

  def check_funds(self, amount):
    # transfer and withdraw should use this ???
    funds = sum([i["amount"] for i in self.ledger])
    if amount > funds:
      return(False)
    else:
      return(True)

  def get_withdrawls(self):
    withdrawls = []
    for i in self.ledger:
      if "-" in str(i["amount"]):
        withdrawls.append(i["amount"])

    return(abs(sum(withdrawls)))
      
    
def create_spend_chart(categories):
  spent_amounts = []
    # Get total spent in each category
  for category in categories:
      spent = 0
      for item in category.ledger:
          if item["amount"] < 0:
              spent += abs(item["amount"])
      spent_amounts.append(round(spent, 2))

  # Calculate percentage rounded down to the nearest 10
  total = round(sum(spent_amounts), 2)
  spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))

  # Create the bar chart substrings
  header = "Percentage spent by category\n"

  chart = ""
  for value in reversed(range(0, 101, 10)):
      chart += str(value).rjust(3) + '|'
      for percent in spent_percentage:
          if percent >= value:
              chart += " o "
          else:
              chart += "   "
      chart += " \n"

  footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
  descriptions = list(map(lambda category: category.name, categories))
  max_length = max(map(lambda description: len(description), descriptions))
  descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
  for x in zip(*descriptions):
      footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

  return (header + chart + footer).rstrip("\n")