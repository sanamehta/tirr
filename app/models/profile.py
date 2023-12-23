# app/models/profile.py
from enum import Enum
from app import db

class IndustryEnum(Enum):
    AGRICULTURE = "Agriculture"
    BUSINESS_AND_PRODUCT = "Business and Product"
    COMMUNICATION_AND_MEDIA = "Communication and Media"
    HI_TECH = "Hi-Tech"
    CONSTRUCTION = "Construction"
    CONSUMER_PRODUCT = "Consumer Product"
    MINING = "Mining"
    TRANSPORTATION = "Transportation"
    UTILITY = "Utility"
    BUSINESS_AND_SERVICES = "Business & Services"
    HEALTHCARE = "Healthcare"
    UNASSIGNED = "Unassigned"
    TRADE = "Trade"

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    industry = db.Column(db.Enum(IndustryEnum), nullable=False)
    payment_history = db.Column(db.String(50), nullable=False)
    audited_balance_sheet = db.Column(db.String(3), nullable=False)
    balance_sheet_time = db.Column(db.String(10), nullable=False)
    use_interim_financial_statements = db.Column(db.String(3), nullable=False)
    years_in_business = db.Column(db.String(10), nullable=False)
    prior_bankruptcy = db.Column(db.String(3), nullable=False)
    tax_liens_legal_actions = db.Column(db.String(3), nullable=False)
    management = db.Column(db.String(50), nullable=False)
    first_interview_approach = db.Column(db.String(50), nullable=False)
    guarantors = db.Column(db.String(50), nullable=True)
    guarantor_net_worth = db.Column(db.String(50), nullable=True)
    guarantor_stake = db.Column(db.String(50), nullable=True)
    primary_residence = db.Column(db.String(50), nullable=True)

