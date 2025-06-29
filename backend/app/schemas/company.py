from enum import Enum as PyEnum
from datetime import datetime
from pydantic import BaseModel, HttpUrl
from typing import Optional, List

# Enums for company status and stage
class CompanyStage(str, PyEnum):
    IDEA = "idea"
    PRE_SEED = "pre_seed"
    SEED = "seed"
    SERIES_A = "series_a"
    SERIES_B = "series_b"
    SERIES_C = "series_c"
    SERIES_D = "series_d"
    SERIES_E = "series_e"
    SERIES_F = "series_f"
    IPO = "ipo"
    ACQUIRED = "acquired"
    DEFUNCT = "defunct"

class CompanyStatus(str, PyEnum):
    ACTIVE = "active"
    ACQUIRED = "acquired"
    DEFUNCT = "defunct"
    STEALTH = "stealth"

class RevenueStage(str, PyEnum):
    PRE_REVENUE = "pre_revenue"
    EARLY_REVENUE = "early_revenue"
    GROWING_REVENUE = "growing_revenue"
    PROFITABLE = "profitable"
    UNKNOWN = "unknown"

class RemotePolicy(str, PyEnum):
    REMOTE_FIRST = "remote_first"
    HYBRID = "hybrid"
    ON_SITE = "on_site"
    FLEXIBLE = "flexible"


class CompanyBase(BaseModel):
    name: str
    legal_name: Optional[str] = None
    tagline: Optional[str] = None
    description: Optional[str] = None
    # website: Optional[HttpUrl] = None
    headquarters_country: str
    stage: CompanyStage
    status: CompanyStatus = CompanyStatus.ACTIVE
    
class CompanyCreate(CompanyBase):
    slug: str
    founded_year: Optional[int] = None
    employee_count_min: Optional[int] = None
    employee_count_max: Optional[int] = None
    
class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    tagline: Optional[str] = None
    description: Optional[str] = None
    website: Optional[HttpUrl] = None
    stage: Optional[CompanyStage] = None
    status: Optional[CompanyStatus] = None
    is_hiring: Optional[bool] = None
    employee_count_min: Optional[int] = None
    employee_count_max: Optional[int] = None
    
class CompanyResponse(CompanyBase):
    id: str
    slug: str
    founded_year: Optional[int]
    employee_count_min: Optional[int]
    employee_count_max: Optional[int]
    total_funding_usd: Optional[float]
    is_hiring: bool
    is_verified: bool
    view_count: int
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True