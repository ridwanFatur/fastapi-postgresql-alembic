from fastapi import FastAPI
from api import user
from db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CV Insight AI",
              version="1.0.0", redirect_slashes=False)


@app.get("/")
async def root():
    return {"message": "App is Ready"}
  
app.include_router(user.router)