# def main():
#     print("Hello from fastapi-learning!")

# if __name__ == "__main__":
#     main()

#-----------------------------------------------
# import sys
# print(sys.executable)
#-----------------------------------------------

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "This is my first API"}

@app.get("/name")
def read_root1():
    return {"message": "Hi Mithra"}

