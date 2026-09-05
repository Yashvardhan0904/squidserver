from sqlalchemy import Column, Integer, String, Boolean
from acmproj.app.core.database import Base

class Player(Base):
    __tablename__ = "squid_players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    score = Column(Integer, default=0)
    is_alive = Column(Boolean, default=True)