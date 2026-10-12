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

        <a href="/apply/leave"><button>休暇申請</button></a><br>
        <a href="/apply/late"><button>遅刻・早退申請</button></a><br>
        <a href="/apply/holidaywork"><button>休日出勤申請</button></a><br>
        <a href="/apply/address"><button>住所変更申請</button></a><br>
        <a href="/apply/name"><button>氏名変更申請</button></a><br>
        <a href="/apply/commute"><button>通勤経路変更申請</button></a><br>
    </body>
    </html>
    """
@router.get("/apply/address", response_class=HTMLResponse)
async def apply_address():
    return """
    <html><body>
        <h2>住所変更申請</h2>
        <form action="/apply/address/submit" method="post">
            <label>新住所：</label><br>
            <textarea name="address" rows="3"></textarea><br><br>

            <label>変更日：</label>
            <input type="date" name="date"><br><br>

            <button type="submit">申請する</button>
        </form>
    </body></html>
    """
@router.get("/apply/commute", response_class=HTMLResponse)
async def apply_commute():
    return """
    <html><body>
        <h2>通勤経路変更申請</h2>
        <form action="/apply/commute/submit" method="post">
            <label>新経路：</label><br>
            <textarea name="route" rows="4"></textarea><br><br>

            <label>変更日：</label>
            <input type="date" name="date"><br><br>

            <button type="submit">申請する</button>
        </form>
    </body></html>
    """
@router.get("/apply/holidaywork", response_class=HTMLResponse)
async def apply_holidaywork():
    return """
    <html><body>
        <h2>休日出勤申請</h2>
        <form action="/apply/holidaywork/submit" method="post">
            <label>出勤日：</label>
            <input type="date" name="date"><br><br>

            <label>勤務時間：</label>
            <input type="time" name="start"> 〜 <input type="time" name="end"><br><br>

            <label>理由：</label><br>
            <textarea name="reason" rows="4"></textarea><br><br>

            <button type="submit">申請する</button>
        </form>
    </body></html>
    """
@router.get("/apply/holidaywork", response_class=HTMLResponse)
async def apply_holidaywork():
    return """
    <html><body>
        <h2>休日出勤申請</h2>
        <form action="/apply/holidaywork/submit" method="post">
            <label>出勤日：</label>
            <input type="date" name="date"><br><br>

            <label>勤務時間：</label>
            <input type="time" name="start"> 〜 <input type="time" name="end"><br><br>

            <label>理由：</label><br>
            <textarea name="reason" rows="4"></textarea><br><br>

            <button type="submit">申請する</button>
        </form>
    </body></html>
    """
@router.get("/apply/late", response_class=HTMLResponse)
async def apply_late():
    return """
    <html><body>
        <h2>遅刻・早退申請</h2>
        <form action="/apply/late/submit" method="post">
            <label>種別：</label>
            <select name="type">
                <option value="late">遅刻</option>
                <option value="early">早退</option>
            </select><br><br>

            <label>日時：</label>
            <input type="datetime-local" name="datetime"><br><br>

            <label>理由：</label><br>
            <textarea name="reason" rows="4"></textarea><br><br>

            <button type="submit">申請する</button>
        </form>
    </body></html>
    """
@router.get("/apply/leave", response_class=HTMLResponse)
async def apply_leave():
    return """
    <html><body>
        <h2>休暇申請</h2>
        <form action="/apply/leave/submit" method="post">
            <label>休暇種別：</label>
            <select name="type">
                <option value="paid">有給休暇</option>
                <option value="special">特別休暇</option>
                <option value="absence">欠勤</option>
            </select><br><br>

            <label>開始日：</label>
            <input type="date" name="start"><br><br>

            <label>終了日：</label>
            <input type="date" name="end"><br><br>

            <label>理由：</label><br>
            <textarea name="reason" rows="4"></textarea><br><br>

            <button type="submit">申請する</button>
        </form>
    </body></html>
    """
@router.get("/apply/name", response_class=HTMLResponse)
async def apply_name():
    return """
    <html><body>
        <h2>氏名変更申請</h2>
        <form action="/apply/name/submit" method="post">
            <label>新氏名：</label>
            <input type="text" name="new_name"><br><br>

            <label>変更日：</label>
            <input type="date" name="date"><br><br>

            <button type="submit">申請する</button>
        </form>
    </body></html>
    """
