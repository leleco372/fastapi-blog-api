from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router

app = FastAPI(tittle="curso api - segurança")
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="info", reload=True)

"""
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzkwOTAzMDc0LCJpYXQiOjE3OTAyOTgyNzQsInN1YiI6IjIifQ.pucSDNn1z8YwJX3-ukxaTMKZiH9EFlvJcXwfI2GLIiI
tipo: bearer
"""