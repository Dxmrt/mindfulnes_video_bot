from fastapi import FastAPI

from main import run_bot

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Mindfulness Video Bot API"}

@app.post("/run")
def run():
    run_bot()
    return {"status": "Bot started!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
