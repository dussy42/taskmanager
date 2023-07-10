import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('discount-planner')

print("welcome🎈 to the shop arena 👌 We give you discounted prices lower than the market price💕")
def calculate_discounted_price(price, discount_rate):
    discount_amount = price * discount_rate
    discounted_price = price - discount_amount
    return discounted_price


def get_data():
    # Get user input
    product_name = input("Enter the product name: ")
    product_price = float(input("Enter the product price: "))

    # Define the discounts for each season
    season_discounts = [
        {"season": "summer", "discount_rate": 0.1},   # 10% off in summer
        {"season": "Autumn", "discount_rate": 0.15},  # 15% off in autumn
        {"season": "winter", "discount_rate": 0.2},   # 20% off in winter
        {"season": "spring", "discount_rate": 0.1}    # 10% off in spring
    ]

    # Calculate discounted price for each season
    discounted_prices = [product_name, str(product_price)]
    for discount in season_discounts:
        discount_rate = discount["discount_rate"]
        discounted_price = calculate_discounted_price(
            product_price, discount_rate)
        discounted_prices.append(str(discounted_price))

    return discounted_prices


def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    sales_worksheet = SHEET.worksheet("price")
    sales_worksheet.append_row(data)


def print_all_products(products):
    print("Hurray🎶 here are the best offer for All Products you wanted:")
    for product in products:
        print(product)


def main():
    products = []
    while True:
        discounted_prices = get_data()
        products.append(discounted_prices)
        update_sales_worksheet(discounted_prices)

        print_all_products(products)

        choice = input("Enter 'Y' to enter another product or any other key to exit: ")
        if choice.upper() != 'Y':
            break

main()
