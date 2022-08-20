from fastapi import FastAPI, Depends
from typing import Union, Optional, List 
from pydantic import BaseModel, Field
from database import dbSession
app = FastAPI()


# model 
class Student(BaseModel):
    name: str = Field(max_length=14, title="username")
    age : int = Field(title="Student age should be greater than 20", gt=20)
    course_id: int
    courses : List[int] = [] 

class CreateStudent(BaseModel):
    username: str
    password: str

class Response(BaseModel):
    username: str
  
#path - /
#  http://locahost:8000/

# path --completed
# Query - 
# path parameters
# path/{name_path}
# request body
#  Fields 
# validation - resquest body validation 

@app.get('/users')
def root():
    return {"message": "success"}

@app.get('/users/{user_id}')
def home(user_id: int):

    return {"message": user_id }

# http://locahost:8000/course/?name="IT"
@app.get('/course/{course_id}')
def query_me(course_id,name: Optional[str] ):
    return {"query-message": name, "message":course_id}


# request body
@app.post("/user-create")
def create_user(user: Student  ):
    if user.name == "macos":
        return {'username': user.name}
    return {'message': "This user is not found"}

#  adding the path parameter, query and the request body 

@app.put("/upadte-student/{student_id}", response_model = Response)
def update_student(student_id: int, query: Optional[str], user: CreateStudent ) -> Response:
    #  different logic 
    return user 

#  dependencies  ---> callable in python --> class , function, instance of a class 
#  dependable function 
def verify_token(query: Optional[str]="TokenSecurity"):
    if query  == "TokenSecurity":
        return {'message':"successful"}
    else :
        return {"message": "failed"}


fake_db = [{"fruit": "Apple"}, {"fruit":"Orange"}, {"fruit":"Grapes"}]


#  dependable class 

class Verify_Token_:
    def __init__(self,id: Optional[int],query:str= "TokenSecurity"):
        self.query = query
        self.id = id 

#  obj = Verify_Token_()
#  obj.id 
#  obj.method()

# 

#  shortcut 
@app.get("/token/")
def verify_user_token(obj_verify_token: Verify_Token_  = Depends()) :
    response = []

    if obj_verify_token.query == "TokenSecurity":
        if obj_verify_token.id < len(fake_db):
            response.append(fake_db[obj_verify_token.id])
    return response

    # if q_params is None:
    #     return []
    # return q_params


# sub-dependencies
# a -> b -> c -> d 
#  dependable dependant

#  dependable function
def query_extractor(query: str):
    return query

#  dependable and dependant function 
def query_cookies_extractor(cookies_param : Optional[str], query_params : str = Depends(query_extractor, use_cache = False)):
    if not query_params:
        return cookies_param
    return query_params

@app.get('/token/items/')    
def extract_query(query_items : str = Depends(query_cookies_extractor,use_cache= False )):
    return {'message':query_items }


#  yielding -- >  allows extra steps to be performed on dependencies 
def get_db():
    db = dbSession()
    try:
       yield  db
    finally:
        db.close()


#  
def create_user(db: Session= Depends(get_db) ):
    # user = db.USerModel().filter()
    # db.commit()
    # db.refresh(user)
    # return user
