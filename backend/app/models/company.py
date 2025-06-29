import uuid
from app.database import Base
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, Boolean, Numeric, JSON
from app.schemas.company import RemotePolicy,CompanyStage,CompanyStatus,RevenueStage

# SQLAlchemy Model
class Company(Base):
    __tablename__ = "companies"
    
    # Primary Key
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # Basic Company Information
    name = Column(String(200), nullable=False, index=True)
    # slug = Column(String(200),nullable=True)
    legal_name = Column(String(200), nullable=True)
    tagline = Column(String(500), nullable=True)
    description = Column(Text, nullable=True)
    
    # # Web Presence
    # website = Column(String(500), nullable=True)
    # careers_page = Column(String(500), nullable=True)
    # linkedin_url = Column(String(500), nullable=True)
    # twitter_handle = Column(String(100), nullable=True)
    # github_org = Column(String(200), nullable=True)
    
    # # Location Information
    # headquarters_city = Column(String(100), nullable=True)
    # headquarters_state = Column(String(100), nullable=True)
    headquarters_country = Column(String(100), nullable=False, index=True)
    # incorporation_country = Column(String(100), nullable=True)
    # is_remote_friendly = Column(Boolean, default=False)
    # remote_policy = Column(Enum(RemotePolicy), nullable=True)
    # office_locations = Column(JSON, nullable=True)  # Array of office locations
    
    # Company Stage and Status
    stage = Column(Enum(CompanyStage), nullable=False, index=True)
    status = Column(Enum(CompanyStatus), default=CompanyStatus.ACTIVE, index=True)
    
    # # Founding Information
    # founding_date = Column(DateTime, nullable=True, index=True)
    # founded_year = Column(Integer, nullable=True, index=True)
    
    # # Team and Size
    # employee_count_min = Column(Integer, nullable=True)
    # employee_count_max = Column(Integer, nullable=True)
    # employee_count_exact = Column(Integer, nullable=True)
    # is_hiring = Column(Boolean, default=False, index=True)
    
    # # Financial Information
    # total_funding_usd = Column(Numeric(15, 2), nullable=True)
    # latest_valuation_usd = Column(Numeric(15, 2), nullable=True)
    # revenue_stage = Column(Enum(RevenueStage), nullable=True)
    # is_profitable = Column(Boolean, nullable=True)
    
    # # Market and Business
    # business_model = Column(String(100), nullable=True)  # B2B, B2C, B2B2C, etc.
    # target_market = Column(String(200), nullable=True)
    
    # # Company Culture and Benefits
    # work_life_balance_rating = Column(Numeric(3, 2), nullable=True)  # 1.00 to 5.00
    # glassdoor_rating = Column(Numeric(3, 2), nullable=True)
    # benefits_summary = Column(Text, nullable=True)
    # company_values = Column(JSON, nullable=True)  # Array of values
    
    # # Diversity and Inclusion
    # diversity_commitment = Column(Text, nullable=True)
    # women_leadership_percentage = Column(Integer, nullable=True)
    
    # # Contact Information
    # contact_email = Column(String(200), nullable=True)
    # application_email = Column(String(200), nullable=True)
    # hr_contact = Column(String(200), nullable=True)
    
    # # SEO and Discovery
    # keywords = Column(JSON, nullable=True)  # Array of keywords for search
    # logo_url = Column(String(500), nullable=True)
    # cover_image_url = Column(String(500), nullable=True)
    
    # # Analytics and Tracking
    # view_count = Column(Integer, default=0)
    # application_count = Column(Integer, default=0)
    # bookmark_count = Column(Integer, default=0)
    
    # # Administrative
    # is_verified = Column(Boolean, default=False)
    # is_featured = Column(Boolean, default=False)
    # is_sponsored = Column(Boolean, default=False)
    # admin_notes = Column(Text, nullable=True)
    
    # # Timestamps
    # created_at = Column(DateTime, default=func.now(), nullable=False)
    # updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    # last_activity_at = Column(DateTime, nullable=True)
    
    # # Data Sources and Attribution
    # data_source = Column(String(100), nullable=True)  # manual, crunchbase, etc.
    # external_ids = Column(JSON, nullable=True)  # {"crunchbase": "id", "linkedin": "id"}