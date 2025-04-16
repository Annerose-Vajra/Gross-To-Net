from pydantic import BaseModel

class GrossToNetRequest(BaseModel):
    gross_salary: float
    region: str

class GrossToNetResponse(BaseModel):
    net_salary: float
    insurance: float
    personal_income_tax: float
    total_deductions: float