def wizard_inventory(inventory_logs):
    inventory = {}
    for log in inventory_logs:
        item = log['item']
        quantity = log['quantity']
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
        if inventory[item] <= 0:
            del inventory[item]
    return inventory