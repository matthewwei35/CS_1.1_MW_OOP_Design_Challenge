# ------------
# Sandwich.py
# ------------

# Class Sandwich
class Sandwich:
  def __init__(self, name, price):
    self.name = name
    self.price = price
    self.ingredients = list()

  def add_ingredients(self, bread, sauce, filling):
    self.ingredients.extend([bread, sauce, filling])

  def remove_ingredient(self, name):
    self.ingredients.remove(name)

if __name__ == "__main__":
  sandwich = Sandwich("Meatball", 6.99)
  sandwich.add_ingredients("French", "Marinara", "Meatballs")
  print(sandwich.ingredients)
  sandwich.remove_ingredient("Meatballs")
  print(sandwich.ingredients)
  