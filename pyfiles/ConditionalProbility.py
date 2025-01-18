from numpy import random

totals = {
    20: 0,
    30: 0,
    40: 0,
    50: 0,
    60: 0,
    70: 0,
}
purchases = {
    20: 0,
    30: 0,
    40: 0,
    50: 0,
    60: 0,
    70: 0,
}

totalPurchases = 0
for _ in range(10000):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
    purchaseProbility = float(ageDecade) / 100.0
    totals[ageDecade] += 1
    if (random.random() < purchaseProbility):
        totalPurchases += 1
        purchases[ageDecade] += 1


def purchaseForAge(age):
    return str(float(purchases[age]) / float(totals[age]) * 100) + '%'

def purchaseForTotal(age):
    return str(float(purchases[age]) / 100) + '%'

print(purchaseForTotal(70))
print(purchaseForAge(20))
