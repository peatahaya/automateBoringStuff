def displayInventory(inventory):
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(f'{k}: {v}')
    print(f"Total number of items: {item_total}")

stuff = {'rope': 1, 'torch': 6, 
         'gold coin': 42, 'dagger': 1, 
         'arrow': 12}

# displayInventory(stuff)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    displayInventory(inventory)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 
              'gold coin', 'gold coin', 'ruby']

addToInventory(inv, dragonLoot)