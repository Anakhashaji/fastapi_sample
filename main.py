from fastapi import FastAPI
from model import Product
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
def greet():
    return "welcome"

products=[
    Product(id=1,name="phone",description="abcc",price=12,quantity=12000),
    Product(id=2,name="phone",description="abcc",price=12,quantity=12000),
    Product(id=3,name="phone",description="abcc",price=12,quantity=12000),
  
  
  
]

@app.get("/products")
def get_all_products():
    return products


@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id == id:
            return product


    return "product not found"

@app.post("/product")
def add_product(Product:Product):
    products.append(Product)
    return products





# @app.get("/favicon.ico", include_in_schema=False)
# def favicon():
#     return PlainTextResponse("")
