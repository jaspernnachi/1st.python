print('Welcome to LTDPYTHON STORE')
name_of_customer= input('Enter your name: ')
print((f'HELLO, {name_of_customer}'))
purchase_amount= float(input('Enter purchase amount: $'))

if purchase_amount < 100:
    print('NO DISCOUNT')
elif purchase_amount ==100 or purchase_amount <= 500:
    discount= 10/100 * purchase_amount
    print(f'You have received discount of 10%: ${discount:.2f}')
elif purchase_amount > 500:
 discount= 20/100 * purchase_amount
print(f'You have recieved discount of 20%: ${discount:.2f}')
discounted_amount = purchase_amount - discount

print(f'Discounted amount: ${discounted_amount:.3f}')
if discounted_amount < 200:
   tax = discounted_amount * 0.05
   print(f'Tax for discount above $200: ${tax:.2f}')

   final_amount = discounted_amount + tax
   print(f'Final amount: ${final_amount:.2f}')