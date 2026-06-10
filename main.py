from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
from models import User, Product
from schemas import UserCreate, ProductCreate

Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-Commerce Backend API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "E-Commerce Backend API Running"}

# User Registration
@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()

    return {"message": "User Registered Successfully"}

# Add Product
@app.post("/products")
def add_product(product: ProductCreate,
                db: Session = Depends(get_db)):

    new_product = Product(
        name=product.name,
        description=product.description,
        price=product.price
    )

    db.add(new_product)
    db.commit()

    return {"message": "Product Added"}

# Get Products
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()