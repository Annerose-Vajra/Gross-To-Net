from src.core.net_ease.controller import gross_to_net
from src.core.net_ease.entities import GrossToNetRequest, GrossToNetResponse

def handle_gross_to_net(req: GrossToNetRequest) -> GrossToNetResponse:
    result = gross_to_net(req.gross_salary, req.region)
    return GrossToNetResponse(**result)


# src/api/routers/net_ease.py
from fastapi import APIRouter
from src.core.net_ease.entities import GrossToNetRequest, GrossToNetResponse
from src.core.net_ease.controller import handle_gross_to_net

router = APIRouter()

@router.post("/gross-to-net", response_model=GrossToNetResponse)
def gross_to_net_api(req: GrossToNetRequest):
    return handle_gross_to_net(req)