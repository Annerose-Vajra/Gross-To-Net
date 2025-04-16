# src/api/routers/net_ease_excel_router.py

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from src.core.net_ease.services import gross_to_net
import pandas as pd
import os
import uuid

router = APIRouter()

@router.post("/upload-excel/")
async def upload_excel(file: UploadFile = File(...)):
    # Tạo tên file tạm duy nhất
    temp_filename = f"temp_{uuid.uuid4().hex}_{file.filename}"

    try:
        # Ghi dữ liệu file upload vào file tạm
        with open(temp_filename, "wb") as buffer:
            buffer.write(await file.read())

        # Đọc file Excel
        df = pd.read_excel(temp_filename, engine='openpyxl')

        # Kiểm tra các cột bắt buộc
        if 'gross_salary' not in df.columns or 'region' not in df.columns:
            os.remove(temp_filename)
            return JSONResponse(
                status_code=400,
                content={"error": "Excel file must contain 'gross_salary' and 'region' columns."}
            )

        # Tính toán
        results = df.apply(
            lambda row: gross_to_net(row['gross_salary'], row['region']),
            axis=1, result_type='expand'
        )
        df_result = pd.concat([df, results], axis=1)

        # Xuất kết quả ra file
        output_filename = f"output_{uuid.uuid4().hex}.xlsx"
        df_result.to_excel(output_filename, index=False)

        # Xoá file tạm
        os.remove(temp_filename)

        # Trả file kết quả
        return FileResponse(
            output_filename,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": f"attachment; filename=net_salaries.xlsx"}
        )

    except Exception as e:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
        return JSONResponse(status_code=500, content={"error": str(e)})
