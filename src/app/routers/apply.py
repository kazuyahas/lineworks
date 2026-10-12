from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/apply", response_class=HTMLResponse)
async def apply_top():
    return """
    <html>
    <head>
        <title>申請メニュー</title>
        <style>
            body { font-family: sans-serif; padding: 30px; }
            .menu { margin: 10px 0; }
            button {
                width: 260px;
                padding: 12px;
                font-size: 16px;
                margin: 6px 0;
            }
        </style>
    </head>
    <body>
        <h2>申請メニュー</h2>
        <p>実施したい申請を選択してください。</p>

        <div class="menu">
            <a href="/apply/leave"><button>休暇申請</button></a><br>
            <a href="/apply/late"><button>遅刻・早退申請</button></a><br>
            <a href="/apply/holidaywork"><button>休日出勤申請</button></a><br>
            <a href="/apply/address"><button>住所変更申請</button></a><br>
            <a href="/apply/name"><button>氏名変更申請</button></a><br>
            <a href="/apply/commute"><button>通勤経路変更申請</button></a><br>
        </div>
    </body>
    </html>
    """
