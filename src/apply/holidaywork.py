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
