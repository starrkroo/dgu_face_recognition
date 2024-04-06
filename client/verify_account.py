import requests

user_image_bytes = open("faces/adr.jpg", 'rb').read()

payload = {
    "uniqcode": "yYjQz3vV9tAZE67ECsbbRAsnhLPf1mc8"
}

files = {
    "user_image_bytes": user_image_bytes
}

r = requests.post("http://127.0.0.1:8000/", data=payload, files=files)
print(r.text)