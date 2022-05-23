import json
from controllers import main

def get_all_products(): 
    """
        This function lists all the products
    """
    try:
        with open("app\products.json", encoding="utf-8") as product_file:
            data = json.load(product_file)
            return data
    except:
        main.create_products_json()
        return "Please, Try Again!"

def get_best_sellers(): 
    """
        This function lists all the best-sellers products
    """
    products = get_all_products()
    best_sellers = {}
    for x in products:
        try:
            if products[x]['best_seller'] == True:
                best_sellers[x] = products[x]
            else:
                continue
        except Exception:
            return "Please, Try Again!"
    return best_sellers

def get_by_rating(rating: float): 
    """
        This function list all higher rating than typed value
    """
    products = get_all_products()
    product_by_rating = {}
    for x in products:
        try:
            if float(products[x]['rating']) > rating:
                product_by_rating[x] = products[x]
            else:
                continue
        except Exception:
            return "Please, Try Again!"
    return product_by_rating

def get_by_name(name: str): 
    """
        This function lists all products with the same typed name, could be more than one
    """
    products = get_all_products()
    product_by_name = {}
    for x in products:
        try:
            if name in products[x]['name'].title():
                product_by_name[x] = products[x]
            elif name == products[x]['name'].title():
                product_by_name[x] = products[x]
            else:
                continue
        except Exception:
            return "Please, Try Again!"
    return product_by_name