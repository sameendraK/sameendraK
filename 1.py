#1.py

products={"dal":23,"maida":32,"sugar":54,"toordal":31,"oil":170,"atta":43,"rice":55,"chocolate":10,"biscuits":20,"perfume":32,"deo":23,"aftershave":94,"nut":95}

keys_of_products=products.keys()

gst={'dal':5, 'maida':5, 'sugar':5, 'toordal':5, 'oil':5, 'atta':5, 'rice':5, 'chocolate':8, 'biscuits':8, 'perfume':18, 'deo':18, 'aftershave':18, 'nut':8}

print(keys_of_products)

bill="product\tquantity\tcost\tgst_perc\tgst_of_item\tcost_cum_gst\titem_total"

def item_total1(product,quantity):
    global bill
    cost=int(products.get(product))
    bill+=str(cost)+"\t"

    gst_perc=int(gst.get(product))
    bill+=str(gst_perc)+"\t"

    gst_of_item=(cost*gst_perc)/100
    bill+=str(gst_of_item)+"\t"
    
    cost_cum_gst=cost+gst_of_item
    bill+=str(cost_cum_gst)+"\t"
    
    item_total=cost_cum_gst*quantity
    bill+=str(item_total)+"\n"
    
    print ("the item total is:" ,item_total)
    
    return item_total
	
	
product=input("enter the product  ")
quantity=int(input("Enter the quantity  "))

bill+=product+"\t"
bill+=str(quantity)+"\t"

item_total=item_total1(product,quantity)

grand_total=0.0

grand_total=grand_total+item_total;

con=input("Enter yes to continue and no to stop ")
while con=="yes":
    product=input("enter the product  ")
    quantity=int(input("Enter the quantity  "))

    bill+=product+"\t"
    bill+=str(quantity)+"\t"

    item_total=item_total1(product,quantity)

    grand_total=grand_total+item_total;

    con=input("Enter yes to continue and no to stop ")
else:  
    print("Thanks for shopping")
    print(bill)
    print("Grand total is : \t\t\t\t%f "%grand_total)
    print("Good Bye ")



"""a user in grocery strores buys some products 
the products are divided into 3 subcategories
1.luxury
2.snacks
3.daily needs
when a user buys a product , the prograrm must show 
the product name, how many peices of the product he brought , the price of each product and CGST,SGST
"""



"""so,firsrt we create 3 userdefined functions to store the prices,products and the GST's of the product.
after , we create dictonary of each items and when the user inputs quantities, we multiply quantity by price.
we then add GST and find the total.
"""

"""
productname     price   gstinperc   gstamount   price+gst       qty     item_total
productname     price   gstinperc   gstamount   price+gst       qty     item_total
productname     price   gstinperc   gstamount   price+gst       qty     item_total
productname     price   gstinperc   gstamount   price+gst       qty     item_total
productname     price   gstinperc   gstamount   price+gst       qty     item_total
productname     price   gstinperc   gstamount   price+gst       qty     item_total
                                                                        ----------
                                                                        grand_total
                                                                        -----------
"""
