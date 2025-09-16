import io
import base64
import qrcode


def make_qr_base64(payload: str) -> str:
    """
    Generate a QR code PNG (Base64 string without data URI prefix).
    """
    img = qrcode.make(payload)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    b64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return b64