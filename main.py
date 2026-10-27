from fastapi import FastAPI
from database import session, engine
import database_models
from fastapi.middleware.cors import CORSMiddleware
from schema import productcreate

database_models.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products")
def getproduct():
   db = session()
   dbproducts = db.query(database_models.Product).all()
   if dbproducts:
      return dbproducts
   else:
      return ['products not found']
  


@app.get("/products/{id}")
def getoneproduct(id: int):
   db= session()
   dbsingleproduct = db.query(database_models.Product).filter(database_models.Product.id == id).first()
   if dbsingleproduct:
      return dbsingleproduct
   else:
    return ['product not exists']



@app.post('/products')
def createproduct(product: productcreate):
   db = session()
   createdproduct = db.add(database_models.Product(**product.model_dump()))
   db.commit()
   return createdproduct


@app.delete('/products/{id}')
def deleteproduct(id: int):
   db = session()
   dbexist = db.query(database_models.Product).filter(database_models.Product.id == id).first()
   if dbexist:
      db.delete(dbexist)
      db.commit()
      return 'successfully deleted'
   else:
      return ['not found']


@app.put("/products/{id}")
def updateproduct(id: int, product: productcreate):
   db = session()
   dbexist = db.query(database_models.Product).filter(database_models.Product.id == id).first()
   if dbexist:
      dbexist.name = product.name
      dbexist.description = product.description
      dbexist.quantity = product.quantity
      dbexist.price = product.price
      db.commit()
      

   