from dataclasses import dataclass


@dataclass
class CompanyBranchForm:
    city: str
    country: str
    postal_code: str
    address: str
    company_id: int
