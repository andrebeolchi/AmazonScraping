from fastapi import FastAPI
from controllers import main, services
app = FastAPI()

main.create_products_json()

@app.get('/')
def root():
    return{"message": "Welcome to my API!"}

@app.get('/list_products')
def lists_all_products(): 
    """ This function lists all products """
    return services.get_all_products()

@app.get('/list_products/best_selling')
def lists_best_sellers(): 
    """ This function lists all best-sellers products """
    return services.get_best_sellers()

@app.get('/list_products/by_rating')
def lists_by_rating(rating: float): 
    """ This function lists all higher rating than the typed value """
    return services.get_by_rating(rating)

@app.get('/list_products/by_name')
def lists_by_name(name: str): 
    """ This function lists all products with the same typed name, could be more than one product """
    return services.get_by_name(name.title())