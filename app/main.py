from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.users.routes import router as users_routes
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup")
    # scheduler.add_job(my_task, IntervalTrigger(seconds=10))
    scheduler.start()
    
    yield
    
    scheduler.shutdown()
    print("Application shutdown")

app = FastAPI(
    title="Multi-vender Marketplace Application",
    description=(
        "A simple and efficient Multi-vender Marketplace Application API built with FastAPI. "
        "This API allows users to create, retrieve, update, and delete products. "
    ),
    version="1.0.0",
    terms_of_service="https://example.com/terms/",
    contact={
        "name": "Ali Bigdeli",
        "url": "https://thealibigdeli.ir",
        "email": "bigdeli.ali3@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    lifespan=lifespan,
)


app.include_router(users_routes)
