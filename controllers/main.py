import json
import bs4

def get_page(): 
    """
        This function was created to get the HTML page
    """
    with open("pages\content.html",  encoding='UTF-8') as content: # Opens the html file
        soup = bs4.BeautifulSoup(content, 'html.parser') # Parses the HTML
    return soup

def get_raw_products(): 
    """
        This function was created to get the raw products
    """
    soup = get_page() # Gets the page
    raw_div = soup.find_all('div', {'class': 'sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20'}) # Gets the raw products
    return raw_div

def get_products_info(): 
    """
        This function was created to get the products information
    """
    raw_div = get_raw_products() # Gets the raw products
    index = 0 # Index of the Dictionary (Counter)
    products = {} # Dictionary of products
    
    for i in raw_div: # For each product, extract its name, price, rating and if it is best seller or not
        name = " ".join(str(i.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'}).text).split()) # Gets the name and clean the input
        price = " ".join(str(i.find('span', {'class': 'a-price'}).find('span', {'class': 'a-offscreen'}).text).split()).replace("R$ ", "").replace(".","").replace(",",".") # Gets the price and clean the input
        
        try:
            best_seller = True if "Mais vendido" == " ".join(str(i.find('span', {'class': 'a-badge-text'}).text).split()) else False # If "Mais vendido" is in product then best seller is True and clean the input
        except Exception:
            best_seller = False # If "Mais vendido" is not found then best seller False

        rating = " ".join(str(i.find('span', {'class': 'a-icon-alt'}).text).split()).replace(",", ".").rstrip(" de 5 estrelas") # Gets the rating and clean the input

        products[index] = {'name': name, 'price': price, 'best_seller': best_seller,'rating': rating} # Appends to the dictionary using the index counter
        index += 1
    return products

def create_products_json(): 
    """
        This function was made to create a json file containing all the products
    """
    products = get_products_info() # Gets information of products
    with open("app\products.json", mode="w", encoding="utf8") as products_file: # Open/Create the products.json as writ mode with enconding UTF-8
        json.dump(products, products_file, ensure_ascii=False) # Writing the products into the json file

create_products_json()