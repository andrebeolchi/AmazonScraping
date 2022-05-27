# WebScraping with BeautifulSoup and FastAPI

- **app/main.py**
    
    *Responsible for the creation of FastAPI, all of the functions of the API are inside it.*


- **controllers/main.py**
    
     *Responsible mainly for the extraction, cleaning and exporting of the data extracted from **pages/content.html***

- **controllers/services.py**	

    *Responsible for the exporting of the data already filtered as solicited by **app/main.py***
 

## How to use

1. Execute **app/main.py** 

2. If the archive ***products.json*** isn't found, the function **create_products_json** of **controllers/main.py** will be executed. 

3. After that, reload the page and the informations of the specified product(s) will show up.

## Setting up your development environment

### Installing the libraries
At the same directory as this file, run:
  - `pip install pipenv`
  - `pipenv install`

### Running the API for development
Initialize your app using `pipenv`:

- `pipenv shell`

Then run the following commands:

- `uvicorn app.main:app --reload`

And your app will be running on http://localhost:8000/

Tip:

Access http://localhost:8000/docs to use the built-in interface.
