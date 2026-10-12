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
