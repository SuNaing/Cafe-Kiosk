from operator import add


total_bill= 0.00
while True:
    print("1.Black Coffee - $2.50")
    print("2.Vanilla Latte - $4.00")
    print("3.Blueberry Muffin - $3.00")
    print("4.Complete Order (Checkout)")

    customer_choice= int(input("Choose an item from the menu (1-4):"))
    if customer_choice==1:
        total_bill+=2.50
        print("Added Black Coffee.Current total:$",total_bill)
    elif customer_choice==2:
        total_bill+=4.00
        print("Added Vanilla Latte.Current total:$",total_bill)
    elif customer_choice==3:
        total_bill+=3.00
        print("Added Blueberry Muffin.Current total:$",total_bill)
    elif customer_choice==4:
        print("Complete Order.(Checkout).Your toal is:$",total_bill)
        break
    else:
        print("Invalid selection. Please choose a valid menu item.")

