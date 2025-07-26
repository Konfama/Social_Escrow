from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    twitter_handle = Column(String(50), unique=True, nullable=False)
    display_name = Column(String(100))
    reputation_score = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

class Deal(Base):
    __tablename__ = 'deals'
    id = Column(Integer, primary_key=True)
    deal_id = Column(String(20), unique=True, nullable=False)
    buyer_id = Column(Integer, ForeignKey('users.id'))
    seller_id = Column(Integer, ForeignKey('users.id'))
    item_description = Column(Text)
    amount = Column(Integer, nullable=False)
    status = Column(String(20), default='pending_payment')
    fee = Column(Integer, default=500)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    deal_id = Column(Integer, ForeignKey('deals.id'))
    posted_by = Column(Integer, ForeignKey('users.id'))
    media_url = Column(Text)
    media_type = Column(String(10))
    timestamp = Column(DateTime, default=datetime.utcnow)

class Confirmation(Base):
    __tablename__ = 'confirmations'
    id = Column(Integer, primary_key=True)
    deal_id = Column(Integer, ForeignKey('deals.id'))
    confirmed_by = Column(Integer, ForeignKey('users.id'))
    confirmation_type = Column(String(20))
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

class AuditLog(Base):
    __tablename__ = 'audit_logs'
    id = Column(Integer, primary_key=True)
    deal_id = Column(Integer, ForeignKey('deals.id'))
    action = Column(String(50))
    performed_by = Column(Integer, ForeignKey('users.id'))
    details = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
