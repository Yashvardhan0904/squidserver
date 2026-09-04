# src/acmproj/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ACM Squid Game API")

# Configure CORS so your Next.js frontend can communicate smoothly
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "ACM Squid Game Backend is running!"}

@app.get("/api/squid-stats")
async def get_squid_stats():
    # Temporary mock data matching your Next.js frontend structure
    return {
        "survivorCount": 456,
        "eliminatedCount": 0,
        "totalPlayers": 456,
        "contestUrl": ""
    }