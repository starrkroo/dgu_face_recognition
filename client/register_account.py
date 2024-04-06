import requests

accounts_image_bytes = open("faces/normal_photo.jpg", 'rb').read()

payload = {
    "uniqcode": "yYjQz3vV9tAZE67ECsbbRAsnhLPf1mc8"
}

files = {
    "image_account_to_store": accounts_image_bytes,
}

r = requests.post("http://127.0.0.1:8000/register_account", data=payload, files=files)