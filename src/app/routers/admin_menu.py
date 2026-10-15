from fastapi import APIRouter, Request
from app.services.bot import register_persistent_menu,
from app.services.bot import start_work_persistent_menu

router = APIRouter()
PC_URL = "https://lineworks-1.onrender.com/apply"
LIST_URL = "https://lineworks-1.onrender.com/apply"

MENU_DATA = {
    "content": {
        "actions": [
            {
                "type": "uri",
                "label": "申請ＴＯＰ",
                "uri": "https://lineworks-1.onrender.com/apply/"
            }
        ]
    }
}


@router.post("/admin/register_menu")
async def register_menu(request: Request):
    token = request.app.state.access_token
    status, text = register_persistent_menu(MENU_DATA, token)
    return {"status": status, "response": text}


@router.post("/admin/start_work_menu")
async def start_work_menu(request: Request):
    START_WORK_MENU_DATA = {
        "content": {
            "actions": [
                {
                    "type": "message",
                    "label": "勤務開始（在宅）",
                    "text ": "勤務開始　在宅"
                },
                {
                    "type": "message",
                    "label": "勤務開始（出社）",
                    "text ": "勤務開始　出社"
                }
                {
                    "type": "message",
                    "label": "勤務終了（在宅）",
                    "text ": "勤務終了　在宅"
                },
                {
                    "type": "message",
                    "label": "勤務終了（出社）",
                    "text ": "勤務終了　出社"
                }
            ]
        }
    }
    token = request.app.state.access_token
    status, text = start_work_persistent_menu(START_WORK_MENU_DATA, token)
    return {"status": status, "response": text}