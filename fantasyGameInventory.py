# Write your code here :-)
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory():
    print('Inventory:')
    for object, quant in stuff.items():
        print(f'{quant} {object}')
        total = str(sum(stuff.values()))
    print(f'Total number of items: {total}')

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i not in inventory:
            inventory[i]=1
        else:
            inventory[i] += 1

addToInventory(stuff, dragonLoot)
displayInventory()
