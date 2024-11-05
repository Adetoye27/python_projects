'''
Write a code using function that will add items in your grocery cart and return total receipt text

order = {'tomato':30 , 'Thyme': 4.50, 'garlic': 7.5, 'rice':10 , 'onions': 4, 'fish': 9.99}

'''

def generate_receipt(order):
    total = 0
    receipt_lines = []
    for item, price in order.items():
        item_name = item.capitalize()
        line = f"{item_name:<25} ${price:>8.2f}"
        receipt_lines.append(line)
        total += price
    receipt_lines.extend([ "-" * 40, f"TOTAL:{' ' * 19}${total:>8.2f}",
        ""])
    return "\n".join(receipt_lines)



order = {
    'tomato': 30,
    'Thyme': 4.50,
    'garlic': 7.5,
    'rice': 10,
    'onions': 4,
    'fish': 9.99
}

print(generate_receipt(order))