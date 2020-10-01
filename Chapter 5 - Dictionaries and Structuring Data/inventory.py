

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby', 'ruby']

def displayInventory(inventory):
    print('Inventory')
    item_total = 0

    for k, v in inventory.items():
        #Fill this part in
        print(str(v) + ' ' + str(k))
        item_total = item_total + v

    print('Total number of items: ' + str(item_total))




def addToInventory(inventory, addedItems):
    #your code here:
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] = inventory[i] + 1


    return inventory

stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)