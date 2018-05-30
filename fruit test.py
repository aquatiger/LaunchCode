def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = quantity

new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)

#  test that 'strawberries' in new_inventory
'strawberries' in new_inventory
print(new_inventory)

#  test that new_inventory['strawberries'] is 10
print(new_inventory['strawberries'])
add_fruit(new_inventory, 'strawberries', new_inventory['strawberries'] + 25)

#  test that new_inventory['strawberries'] is now 35)
print(new_inventory['strawberries'])

add_fruit(new_inventory, 'strawberries', 10)
