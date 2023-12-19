from aws_lambda_powertools import Logger, Tracer
from boto3.dynamodb.conditions import Attr, Key
import json
import qrcode
from PIL import Image
from io import BytesIO
import base64
import boto3
tracer = Tracer()
logger = Logger()


def generate_qr(sf_id, payload):

    qr_data = payload["id"]
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Convert the image to bytes
    img_byte_array = BytesIO()
    img.save(img_byte_array, format="PNG")
    img_bytes = img_byte_array.getvalue()

    # Encode the image bytes in base64
    encoded_image = base64.b64encode(img_bytes).decode("utf-8")
    return {"data": {"qr_data": qr_data, "sf_id": sf_id, "image": encoded_image}}
