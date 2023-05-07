import requests
import json

def twitter_check(username):
    response = requests.get(f"https://twitter.com/i/api/i/users/username_available.json?username={username}").json()["valid"]
    return response
def insta_checker(username):
    req = requests.get(f"https://www.instagram.com/{username}")
    if req.status_code == 404:
        result = "available"
    elif req.status_code == 200:
        result = "unavailable"
    return result
