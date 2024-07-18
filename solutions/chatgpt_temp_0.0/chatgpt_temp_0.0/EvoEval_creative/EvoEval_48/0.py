def wizard_inventory(inventory_logs):
    inventory = {}
    for log in inventory_logs:
        item = log['item']
        quantity = log['quantity']
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
    final_inventory = {item: quantity for (item, quantity) in inventory.items() if quantity > 0}
    return final_inventory