# ------------
# Order.py
# ------------
from Sandwich import Sandwich

# Class Order
class Order:
  def __init__(self, order_name = "Guest"):
    self.order_name = order_name
    self.sandwiches = list()

  def view_order(self):
    total = 0
    print(f"Thank you for coming, {self.order_name}!")
    for sandwich in self.sandwiches:
      total += float(sandwich.price)
      print(f"{sandwich.name} - {sandwich.price}")
    print(f"Total:  {round(total, 2)}")

  def add_custom_sandwich(self, name, price, bread, sauce, filling):
    new_sandwich = Sandwich(name, price)
    new_sandwich.add_ingredients(bread, sauce, filling)
    self.sandwiches.append(new_sandwich)

  def add_sandwich(self, name, price):
    new_sandwich = Sandwich(name, price)
    self.sandwiches.append(new_sandwich)

  def remove_sandwich(self, name):
    self.sandwiches.remove(name)

if __name__ == "__main__":
  order = Order("Matthew")
  order.add_custom_sandwich("Meatball", 4.99, "French", "Marinara", "Meatballs")
  order.add_custom_sandwich("Meatball", 4.99, "French", "Marinara", "Meatballs")
  order.add_custom_sandwich("Meatball", 4.99, "French", "Marinara", "Meatballs")
  order.view_order()
  