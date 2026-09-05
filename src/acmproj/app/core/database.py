from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from supabase import create_client, Client
from acmproj.app.core.config import settings

# SQLAlchemy Engine for Migrations and ORM models
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Official Supabase Python Client for storage/auth/queries
supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)