from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Smart-Bank API is running 🎉"}

@app.get("/api/health")
def health():
    return {"status": "ok"}
