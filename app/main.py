from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Kvartira ijarasi API ishga tushdi!"}
