'''Problem 1:

Suppose you are buying something online on amazon.com 

On the website, you get
a 15% discount if you are a prime member. Additionally, you are also getting a discount of 8% on the item because it's black Friday sales.

Write a function that takes as input the amount of the asset that you are buying and a logical variable indicating whether you are a prime member applies the discount offered appropriately and returns the result.'''

def shoping(amount, its_prime_member):
    discount = 0
    if its_prime_member:
        discount = amount - (amount * (0.15 + 0.08))
    else:
        discount = amount - (amount * 0.08)
    return discount

print(shoping(2000, True)) 