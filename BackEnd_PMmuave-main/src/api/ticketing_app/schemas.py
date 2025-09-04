# schemas.py - Định nghĩa Pydantic models cho request/response

from pydantic import BaseModel
from typing import List, Optional

# ----------- Vé -----------
class VeBase(BaseModel):
    ten_su_kien: str
    gia: float

class VeCreate(VeBase):
    pass

class VeResponse(VeBase):
    id: int
    qr_code: Optional[str] = None

    class Config:
        orm_mode = True


# ----------- Dòng Hóa Đơn -----------
class DongHoaDonBase(BaseModel):
    ve_id: int
    so_luong: int

class DongHoaDonResponse(DongHoaDonBase):
    id: int

    class Config:
        orm_mode = True


# ----------- Hóa Đơn -----------
class HoaDonBase(BaseModel):
    user_id: int

class HoaDonCreate(HoaDonBase):
    chi_tiet: List[DongHoaDonBase]

class HoaDonResponse(HoaDonBase):
    id: int
    tong_tien: float
    chi_tiet: List[DongHoaDonResponse]

    class Config:
        orm_mode = True
