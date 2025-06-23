# 5. Inventory Matching and Pricing

'''Approach:
 Sort items by price and buy as many units as possible within the budget.
 '''

def process_order(inventory, qty_needed, budget):
    inventory.sort(key=lambda x: x['price'])  # cheapest first

    bought = 0
    cost = 0

    for item in inventory:
        if bought >= qty_needed:
            break
        take = min(item['quantity'], qty_needed - bought)
        if cost + take * item['price'] <= budget:
            bought += take
            cost += take * item['price']
        else:
            can_afford = (budget - cost) // item['price']
            bought += can_afford
            cost += can_afford * item['price']
            break

    if bought == qty_needed:
        return "Order fulfillable"
    elif bought > 0:
        return "Partially fulfillable"
    return "Order impossible"


inventory = [
    {'name': 'A', 'quantity': 5, 'price': 10},
    {'name': 'B', 'quantity': 10, 'price': 7},
    {'name': 'C', 'quantity': 3, 'price': 5}
]

print(process_order(inventory, 10, 75))
