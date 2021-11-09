#item_billing
products={"dal":23,"maida":32,"sugar":54,"toordal":31,"oil":170,"atta":43,"rice":55,"chocolate":10,"biscuits":20,"perfume":32,"deo":23,"aftershave":94,"nut":95}
gst={'dal':5, 'maida':5, 'sugar':5, 'toordal':5, 'oil':5, 'atta':5, 'rice':5, 'chocolate':8, 'biscuits':8, 'perfume':18, 'deo':18, 'aftershave':18, 'nut':8}
keys_of_products=products.keys()
print(keys_of_products)
bill=""
def i_t(product,quantity):
    global bill
    gst_percentage=gst.get(product)
    bill+=str(gst_percentage)+"\t"
    item_cost_per_unit=products.get(product)
    bill+=str(item_cost_per_unit)+"\t"
    item_price=(((item_cost_per_unit*gst_percentage)/100)+item_cost_per_unit)*quantity
    bill+=str(item_price)+"\n"
    return item_price
    
product=input("Enter product  ")
quantity=int(input("Enter Quantity  "))
bill+=(product)
bill+=str(quantity)
item_price=i_t(product,quantity)
total=0 
total=total+item_price;
i_t(product,quantity)
c=input("Press Y to continue and N to end your shopping:  ")
while c=="y":
    product=input("Enter product  ")
    quantity=int(input("Enter Quantity  "))
    bill+=product
    bill+=str(quantity)
    i_t(product,quantity)    
    total=total+item_price;
    c=input("Press Y to continue and N to end your shopping:  ")
else:
    print("Thanks for shopping")
    print(bill)
    print("grand total: %f"%total)