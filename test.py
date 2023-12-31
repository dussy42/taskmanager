def desobj(obj,index=None):

    l =     "\t"
    keys = list(obj.keys())
    for  index , val in enumerate(keys):
        values = obj[val]
        if (type(values) is dict):...
        #   values = f"\n{desobj(values ,True)}"
      
        
        l = f'{l}{f"{index+1}. {val}: {values} "}\n\t'
             
             
        
   

   
  

    return l
# print(desobj({"ss":"ds","SD":"Sd"}),"11"+"11")
products  ={'product_name': 'sss', 'userprice': '22.0', 'discounts': {'summer_discount': '19.8', 'Autumn_discount': '18.7', 'winter_discount': '17.6', 'spring_discount': '19.8'}}

print(f"""

product  :          {products["product_name"]}
userprice:          {products["userprice"]}
discounted price:
{desobj(products["discounts"]) 

                }



""")