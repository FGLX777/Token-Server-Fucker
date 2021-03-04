import requests 
token = input("Token?")
text = input("Text?:")
headers={
    "authorization": f"{token}",
    "content-type": "application/json"
    }
payload={
   "name": f"{text}"
    }
while True:
    requests.post("https://discord.com/api/v8/guilds",json=payload,headers=headers) 
