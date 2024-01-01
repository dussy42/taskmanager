import gspread
import requests
from google.oauth2.service_account import Credentials
import google

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

connectionerror = '''
Connections error....`
Try:

Checking your internet connection
Checking your proxy, firewall
Running Windows Network Diagnostics



'''


SHEET = None


try:
    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('discount-planner')


except (requests.exceptions.ConnectionError):
    print(connectionerror)
except (google.auth.exceptions.TransportError):
    print(connectionerror)
except (Exception):
    print("We an error at our end , sorry for the inconviniences")

print("welcome🎈 to the shop arena 👌 We give you discounted prices lower than the market price💕")
def calculate_discounted_price(price, discount_rate):
    discount_amount = price * discount_rate
    discounted_price = price - discount_amount
    return discounted_price

def getprice(data="Enter the product price: "):
    price = input(data)
    if (price.isnumeric() and float(price) > 0):
        return price

    return getprice("please enter a valid whole number price greater than 0...\n")

def getproduct(data="Enter the product name: "):
    product = input(data)
    if (len(product) < 3 or not product[:3].isalpha()):
        return getproduct("please enter a valid product... a product must begin with first three character...\n")
    return product


def get_data():
    # Get user input
    product_name = getproduct()
    price = getprice()

    product_price = float(price)

    # Define the discounts for each season
    season_discounts = [
        {"season": "summer", "discount_rate": 0.1},   # 10% off in summer
        {"season": "Autumn", "discount_rate": 0.15},  # 15% off in autumn
        {"season": "winter", "discount_rate": 0.2},   # 20% off in winter
        {"season": "spring", "discount_rate": 0.1}    # 10% off in spring
    ]

    # Calculate discounted price for each season
    discounted_prices = {"product_name": product_name,
                         "userprice": str(product_price), "discounts": {}}
    for discount in season_discounts:
        discount_rate = discount["discount_rate"]
        discounted_price = calculate_discounted_price(
            product_price, discount_rate)
        discounted_prices["discounts"][f"{discount['season']}_discount"] = str(
            discounted_price)

    return discounted_prices


def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    sales_worksheet = SHEET.worksheet("price")
    sales_worksheet.append_row(data)
    

def desobj(obj, index=None):
    """
    helps in destructuring the selected obj into a string to increase readbility
    """

    l = "\t"
    keys = list(obj.keys())
    for index, val in enumerate(keys):
        values = obj[val]
        if (type(values) is dict):
            ...

        l = f'{l}{f"{index+1}. {val}: {values} "}\n\t'

    return l



def print_all_products(products):
    print("Hurray🎶 here are the best offer for All Products you wanted:\n")
    print(f"""
product  :          {products["product_name"]}
userprice:          {products["userprice"]}
discounted price:
{desobj(products["discounts"]) }""")
    

def selectproduct(product):
    priceobj = product["discounts"]
    seasons = list(priceobj.keys())
    prices = list(priceobj.values())

    def getpriceindex(data="select product by entering the suitable index: "):
        price = input(data).strip()

        if (price.isnumeric() and int(price) <= 4 and int(price) > 0):
            return int(price)

        return getpriceindex("please enter a valid index...\n")
    pricenum = getpriceindex()
    return [product["product_name"], product["userprice"], prices[pricenum-1]]


def main():
    """starter function for the algorithm"""
   
    while True:
        discounted_prices = get_data()

        print_all_products(discounted_prices)
        selectedproduct = selectproduct(discounted_prices)
        print(selectedproduct,"your selected order is being processed, thank you for your patronage ")
        try:
            update_sales_worksheet(selectedproduct)
        except Exception as e:
            print(e)
        choice = input( "Enter 'Y' to enter purchase another product or any other key to exit: ")
        
        if choice.upper() != 'Y':
            break

main()
