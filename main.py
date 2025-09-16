from fastapi import FastAPI
from model import Product
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
def greet():
    return "welcome"

products=[
    Product(1,"phone","abcc",12,12000),Product(2,"laptop",
            "abcc",12,12000)
]

@app.get("/products")
def get_all_products():
    return products


# @app.get("/favicon.ico", include_in_schema=False)
# def favicon():
#     return PlainTextResponse("")
