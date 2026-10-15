import requests
import os
import json

BASE_API_URL = "https://www.worksapis.com/v1.0"

def register_persistent_menu(menu_data: dict, token: str):
    bot_no = os.environ["LINEWORKS_BOT_NO"]
    url = f"{BASE_API_URL}/bots/{bot_no}/persistentmenu"

    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": f"Bearer {token}"
    }

    resp = requests.post(url, headers=headers, data=json.dumps(menu_data))
    return resp.status_code, resp.text

def start_work_persistent_menu(menu_data: dict, token: str):
    bot_no = os.environ["13353898"]
    url = f"{BASE_API_URL}/bots/{bot_no}/persistentmenu"

    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": f"Bearer {token}"
    }

    resp = requests.post(url, headers=headers, data=json.dumps(menu_data))
    return resp.status_code, resp.text

