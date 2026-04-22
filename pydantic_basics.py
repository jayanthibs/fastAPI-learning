from pydantic import BaseModel, EmailStr

class Person(BaseModel):
    name: str
    age: int
    email: EmailStr

valid_data = Person(name="jayanthi", age=11, email="jayanthi@gmail.com")
print(valid_data)