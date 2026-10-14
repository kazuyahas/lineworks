from fastapi import APIRouter, Request
from app.services.bot import register_persistent_menu

router = APIRouter()
PC_URL = "https://lineworks-1.onrender.com/apply"
LIST_URL = "https://lineworks-1.onrender.com/apply"

MENU_DATA = {
    "content": {
        "actions": [
            {
                "type": "message",
                "label": "申請ＴＯＰ",
                "uri": "https://lineworks-1.onrender.com/apply"
            }
        ]
    }
}


@router.post("/admin/register_menu")
async def register_menu(request: Request):
    token = request.app.state.access_token
    status, text = register_persistent_menu(MENU_DATA, token)
    return {"status": status, "response": text}
