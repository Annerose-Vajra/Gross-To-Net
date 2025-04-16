from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.api.routers import net_ease

app = FastAPI(title="Gross to Net Salary Calculator")

# Include router từ net_ease.py
app.include_router(net_ease.router, prefix="/api/v1", tags=["Salary"])

@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h1>Gross to Net Salary Calculator API</h1><p>Try POST /api/v1/gross-to-net or /api/v1/upload-excel</p>"
