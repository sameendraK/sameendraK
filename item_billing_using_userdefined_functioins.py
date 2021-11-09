#item_billing_using_userdefined_functioins
products={"dal":23,"maida":32,"sugar":54,"toordal":31,"oil":170,"atta":43,"rice":55,"chocolate":10,"biscuits":20,"perfume":32,"deo":23,"aftershave":94,"nut":95}
keys_of_products=products.keys()
gst={'dal':5, 'maida':5, 'sugar':5, 'toordal':5, 'oil':5, 'atta':5, 'rice':5, 'chocolate':8, 'biscuits':8, 'perfume':18, 'deo':18, 'aftershave':18, 'nut':8}
print(keys_of_products)

def item_total1(product,quantity):
    cost=int(products.get(product))
    gst_of_item=int(gst.get(product))
    # print ("The cost of 1 unit of %s is "%product,cost)
    # print ("The G.S.T of 1 unit of  %s is "%product,gst_of_item)
    itemgst=cost*gst_of_item/100
    costgst=cost+itemgst
    item_total=costgst*quantity
    # item_total=cost*quantity
    # print ("the item total is:" ,item_total)
    return item_total
    
"""
def gst_caluculation(product):
    cost=products.get(product)
    gst_percentage=int(gst.get(product))
    gst_of_product=float((cost*gst_percentage)/100)
    return gst_of_product
"""
    
product=input("enter the product  ")
l=[]
o=[]
tot=[]
l.append(product) 
cc=gst_caluculation(product)
o.append(cc)
quantity=int(input("Enter the quantity  "))
item_total=item_total1(product,quantity)
gst_of_i=float(gst_caluculation(product))
con=input("Enter yes to continue and no to stop ")
while con=="yes":
        product=input("enter the product  ")
        cc=gst_caluculation(product)
        o.append(cc)
        l.append(product)
        quantity=int(input("Enter the quantity  "))
        item_total=item_total1(product,quantity)
        con=input("Enter yes to continue and no to stop ")
print(l)
lo=len(l)
print(lo)
for i  in range(0,lo):
    v=products.get(l[i])
    w=gst.get(l[i])
    y=v*quantity
    z=y+o[i]
    tot=[0]
    soi=sum(tot)
    tot.append(y)
    print("product  :  ",l[i])
    print("Cost per unit is: ",v)
    print("qunatiny = ",quantity)
    print("Item total (without G.S.T)is:",y)
    tot.append(y)
    print("Grand total is :",soi)
    print("G.S.T of the item (in percentage)is:",w)
    print("Item price with G.S.T is:",z)
    tot.append(z)
    hes=sum(tot)
    
    print("****************************************************")
else :  
        f=len(tot)
        for i in range(1,f):
            print("GGRRAAMMDDTTOOTTAALL IISSdddddddddddddddddddddddddddddddddddddddddddddddddddd::",hes)
            print("Thanks for shopping ")
    
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
