from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    # Return a welcome message
    pass

# Task 2: Add more endpoints here
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     pass

# @app.post("/items/")
# def create_item(item: dict):
#     pass