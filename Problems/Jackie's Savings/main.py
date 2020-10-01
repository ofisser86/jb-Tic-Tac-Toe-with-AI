def final_deposit_amount(*interest, amount):
    for i in interest:
        amount += amount * (1 * i / 100)
    return round(amount, 2)
