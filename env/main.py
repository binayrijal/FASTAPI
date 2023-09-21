from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def root():
    return {"message":"helloworld"}
#function defination
@app.get("/name")
def my_name(firstname:str,lastname:str):
    full_name=firstname.title()+""+lastname.title()
    return (full_name)
print(my_name("Binay","Rijal"))
