from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from routes.member import router as member_router

from prisma import Prisma

prisma=Prisma()

@asynccontextmanager
async def lifespan(app:FastAPI):
    await prisma.connect()
    yield
    await prisma.disconnect()

app=FastAPI(title="Amazon api",lifespan=lifespan)

#register router
app.include_router(member_router,prefix="/member")

@app.get("/")
async def root():
    members=await prisma.member.find_many()
    print(members)
    return {"message":"API is running"}

if __name__ == "__main__":
    uvicorn.run("app:app",host="127.0.0.1",port=5000,reload=True)