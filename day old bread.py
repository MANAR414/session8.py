each_bread=3.49
discount=6/100
old_bread=int(input("enter no. of old bread:"))
def discount_amount(old_bread):
    if old_bread!=0:
         regular_price=each_bread*old_bread
         discount_amount=regular_price*discount
         price_after_discount=regular_price-discount_amount
         print(f"regular price for the bread is:{regular_price}")
         print(f"there is a discount {discount_amount} bec. it's a day old")
         print(f"So,the total price is:{price_after_discount}") 


discount_amount(old_bread)


