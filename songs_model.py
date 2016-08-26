from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker


from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    create_engine
)
import datetime
import os
import sqlite3
engine = create_engine('sqlite:///lyrics.db', echo=False)

Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class LyricsFind(Base):  
    __tablename__  = "songs"    
    id             = Column(Integer, primary_key=True) 
    track_id     = Column(String(255))                                 
    track_lyrics   = Column(String(255))              
    date_added     = Column(DateTime, default=datetime.datetime.now)

def save_lyric(track_id, track_lyrics):
    lyrics = LyricsFind(track_id = track_id,track_lyrics=track_lyrics)
    session.add(lyrics)
    session.commit()
def clear_lyrics():
    num_rows_deleted = session.query(LyricsFind).delete()
    session.commit()
def fetch_lyric(track_id):
    if session.query(LyricsFind.id).filter_by(track_id = track_id).scalar() is None:
        return False
    finder = session.query(LyricsFind)
    song = finder.filter_by(track_id = track_id).first()
    if(song):
        return song.track_lyrics
    else:
        return None

Base.metadata.create_all(engine)