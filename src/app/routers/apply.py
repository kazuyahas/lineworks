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
        <script>
            function closeWindow() {
                window.open('about:blank','_self').close();
            }
        </script>
    </head>
    <body>
        <h2>申請メニュー</h2>
        <p>実施したい申請を選択してください。</p>

        <a href="/apply/leave"><button>休暇申請</button></a><br>
        <a href="/apply/address"><button>住所変更申請</button></a><br>
        <a href="/apply/name"><button>氏名変更申請</button></a><br>
        <a href="/apply/commute"><button>通勤定期代変更届</button></a><br>
        <a href="/apply/bank"><button>給与・賞与振込口座届</button></a><br>
        <a href="/apply/late"><button>遅刻早退届</button></a><br>

        <br><br>
        <button type="button" onclick="closeWindow()">閉じる</button>
    </body>
    </html>
    """
@router.get("/apply/leave", response_class=HTMLResponse)
async def apply_leave():
    return """
    <html><body>
        <h2>休暇申請</h2>
        <form action="/apply/leave/submit" method="post">

            <input type="hidden" name="applicant_id" value="USER_ID_PLACEHOLDER">
            <input type="hidden" name="apply_date" value="{NOW}">

            <label>承認期限：</label>
            <input type="date" name="approval_deadline"><br><br>

            <label>休暇種類：</label><br>
            <input type="radio" name="leave_type" value="paid"> 有給休暇<br>
            <input type="radio" name="leave_type" value="summer"> 夏季休暇<br>
            <input type="radio" name="leave_type" value="special"> 特別休暇<br>
            <input type="radio" name="leave_type" value="absence"> 欠勤<br><br>

            <label>休暇日：</label>
            <input type="date" name="leave_date"><br><br>

            <label>休暇日数：</label>
            <input type="number" name="leave_days" min="1"><br><br>

            <label>理由：</label><br>
            <textarea name="reason" rows="4"></textarea><br><br>

            <button type="submit">申請する</button>
        </form>

        <br><br>
        <a href="/apply"><button type="button">申請メニューに戻る</button></a>
    </body></html>
    """
@router.get("/apply/address", response_class=HTMLResponse)
async def apply_address():
    return """
    <html><body>
        <h2>住所変更申請</h2>
        <form action="/apply/address/submit" method="post">

            <input type="hidden" name="applicant_id" value="USER_ID_PLACEHOLDER">
            <input type="hidden" name="apply_date" value="{NOW}">

            <label>承認期限：</label>
            <input type="date" name="approval_deadline"><br><br>

            <label>住所変更日：</label>
            <input type="date" name="change_date"><br><br>

            <label>住所形態：</label><br>
            <input type="radio" name="address_type" value="own"> 持ち家<br>
            <input type="radio" name="address_type" value="rent"> 賃貸<br>
            <input type="radio" name="address_type" value="parent"> 親元<br>
            <input type="radio" name="address_type" value="company_house"> 社宅<br>
            <input type="radio" name="address_type" value="company_contract"> 会社契約<br><br>

            <label>通勤経路の変更：</label>
            <input type="checkbox" name="commute_change"><br><br>

            <label>最寄り駅：</label>
            <input type="text" name="nearest_station"><br><br>

            <label>新住所：</label><br>
            <textarea name="new_address" rows="3"></textarea><br><br>

            <label>旧住所：</label><br>
            <textarea name="old_address" rows="3"></textarea><br><br>

            <button type="submit">申請する</button>
        </form>

        <br><br>
        <a href="/apply"><button type="button">申請メニューに戻る</button></a>
    </body></html>
    """
@router.get("/apply/name", response_class=HTMLResponse)
async def apply_name():
    return """
    <html><body>
        <h2>氏名変更届</h2>
        <form action="/apply/name/submit" method="post">

            <input type="hidden" name="applicant_id" value="USER_ID_PLACEHOLDER">
            <input type="hidden" name="apply_date" value="{NOW}">

            <label>承認期限：</label>
            <input type="date" name="approval_deadline"><br><br>

            <label>旧姓：</label>
            <input type="text" name="old_name"><br><br>

            <label>新姓：</label>
            <input type="text" name="new_name"><br><br>

            <label>変更理由：</label><br>
            <textarea name="reason" rows="4"></textarea><br><br>

            <label>変更日：</label>
            <input type="date" name="change_date"><br><br>

            <button type="submit">申請する</button>
        </form>

        <br><br>
        <a href="/apply"><button type="button">申請メニューに戻る</button></a>
    </body></html>
    """
@router.get("/apply/commute", response_class=HTMLResponse)
async def apply_commute():
    return """
    <html><body>
        <h2>通勤定期代変更届</h2>
        <form action="/apply/commute/submit" method="post">

            <input type="hidden" name="applicant_id" value="USER_ID_PLACEHOLDER">
            <input type="hidden" name="apply_date" value="{NOW}">

            <label>承認期限：</label>
            <input type="date" name="approval_deadline"><br><br>

            <label>居住地：</label>
            <input type="text" name="residence"><br><br>

            <label>変更日：</label>
            <input type="date" name="change_date"><br><br>

            <label>変更理由：</label><br>
            <input type="radio" name="change_reason" value="move"> 転居<br>
            <input type="radio" name="change_reason" value="transfer"> 転勤・異動<br>
            <input type="radio" name="change_reason" value="office_move"> 事務所移転<br>
            <input type="radio" name="change_reason" value="price_change"> 料金改定<br>
            <input type="radio" name="change_reason" value="route_change"> 経路変更<br>
            <input type="radio" name="change_reason" value="other"> その他<br><br>

            <label>その他（理由詳細）：</label>
            <input type="text" name="reason_other"><br><br>

            <h3>新区間（電車１）</h3>
            <label>路線名：</label>
            <input type="text" name="train1_line"><br><br>

            <label>区間 開始：</label>
            <input type="text" name="train1_start"><br><br>

            <label>区間 終了：</label>
            <input type="text" name="train1_end"><br><br>

            <label>定期代：</label>
            <input type="number" name="train1_price"><br><br>

            <h3>新区間（電車２）</h3>
            <label>路線名：</label>
            <input type="text" name="train2_line"><br><br>

            <label>区間 開始：</label>
            <input type="text" name="train2_start"><br><br>

            <label>区間 終了：</label>
            <input type="text" name="train2_end"><br><br>

            <label>定期代：</label>
            <input type="number" name="train2_price"><br><br>

            <h3>新区間（電車３）</h3>
            <label>路線名：</label>
            <input type="text" name="train3_line"><br><br>

            <label>区間 開始：</label>
            <input type="text" name="train3_start"><br><br>

            <label>区間 終了：</label>
            <input type="text" name="train3_end"><br><br>

            <label>定期代：</label>
            <input type="number" name="train3_price"><br><br>

            <h3>新区間（バス１）</h3>
            <label>路線名：</label>
            <input type="text" name="bus1_line"><br><br>

            <label>利用区間 開始：</label>
            <input type="text" name="bus1_start"><br><br>

            <label>利用区間 終了：</label>
            <input type="text" name="bus1_end"><br><br>

            <label>定期代：</label>
            <input type="number" name="bus1_price"><br><br>

            <h3>交通用具利用の場合</h3>
            <label>交通用具：</label><br>
            <input type="radio" name="vehicle_type" value="bicycle"> 自転車<br>
            <input type="radio" name="vehicle_type" value="bike"> バイク<br>
            <input type="radio" name="vehicle_type" value="car"> 乗用車<br><br>

            <label>利用区間 開始：</label>
            <input type="text" name="vehicle_start"><br><br>

            <label>利用区間 終了：</label>
            <input type="text" name="vehicle_end"><br><br>

            <label>利用料金：</label>
            <input type="number" name="vehicle_price"><br><br>

            <h3>通勤定期代合計</h3>
            <label>合計金額：</label>
            <input type="number" name="total_price"><br><br>

            <button type="submit">申請する</button>
        </form>

        <br><br>
        <a href="/apply"><button type="button">申請メニューに戻る</button></a>
    </body></html>
    """
@router.get("/apply/bank", response_class=HTMLResponse)
async def apply_bank():
    return """
    <html><body>
        <h2>給与・賞与振込口座届</h2>
        <form action="/apply/bank/submit" method="post">

            <!-- 申請者（非表示） -->
            <input type="hidden" name="applicant_id" value="USER_ID_PLACEHOLDER">

            <!-- 申請日（非表示） -->
            <input type="hidden" name="apply_date" value="{NOW}">

            <label>承認期限：</label>
            <input type="date" name="approval_deadline"><br><br>

            <label>銀行名：</label>
            <input type="text" name="bank_name"><br><br>

            <label>銀行コード：</label>
            <input type="text" name="bank_code"><br><br>

            <label>支店名：</label>
            <input type="text" name="branch_name"><br><br>

            <label>支店コード：</label>
            <input type="text" name="branch_code"><br><br>

            <label>口座番号：</label>
            <input type="text" name="account_number"><br><br>

            <button type="submit">申請する</button>
        </form>

        <br><br>
        <a href="/apply">
            <button type="button">申請メニューに戻る</button>
        </a>
    </body></html>
    """
@router.get("/apply/late", response_class=HTMLResponse)
async def apply_late():
    return """
    <html><body>
        <h2>遅刻早退届</h2>
        <form action="/apply/late/submit" method="post">

            <!-- 申請者（非表示） -->
            <input type="hidden" name="applicant_id" value="USER_ID_PLACEHOLDER">

            <!-- 申請日（非表示） -->
            <input type="hidden" name="apply_date" value="{NOW}">

            <label>承認期限：</label>
            <input type="date" name="approval_deadline"><br><br>

            <label>内容：</label><br>
            <input type="radio" name="type" value="late"> 遅刻<br>
            <input type="radio" name="type" value="early"> 早退<br><br>

            <label>日時：</label>
            <input type="datetime-local" name="datetime"><br><br>

            <label>理由：</label><br>
            <textarea name="reason" rows="4"></textarea><br><br>

            <label>休日出勤日：</label>
            <input type="date" name="holiday_work_date"><br><br>

            <label>振替休日：</label>
            <input type="date" name="substitute_holiday"><br><br>

            <label>休日出勤時の業務内容：</label><br>
            <textarea name="holiday_work_detail" rows="3"></textarea><br><br>

            <label>休日出勤の理由：</label><br>
            <textarea name="holiday_work_reason" rows="3"></textarea><br><br>

            <button type="submit">申請する</button>
        </form>

        <br><br>
        <a href="/apply">
            <button type="button">申請メニューに戻る</button>
        </a>
    </body></html>
    """
