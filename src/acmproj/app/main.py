from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from acmproj.app.core.database import supabase, engine, SessionLocal
from acmproj.app.models.player import Player
from acmproj.app.schemas.player import PlayerResponse

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
    return {
        "survivorCount": 456,
        "eliminatedCount": 0,
        "totalPlayers": 456,
        "contestUrl": ""
    }

@app.get("/api/health-check")
async def health_check():
    try:
        if not supabase:
            raise HTTPException(status_code=500, detail="Supabase client failed to initialize.")

        with engine.connect() as connection:
            db_status = "Connected successfully"
            
        return {
            "status": "healthy",
            "database": db_status,
            "supabase_url_configured": bool(supabase.supabase_url)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Connection failed: {str(e)}")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/players", response_model=list[PlayerResponse])
def get_players(db: Session = Depends(get_db)):
    players = db.query(Player).all()
    return players