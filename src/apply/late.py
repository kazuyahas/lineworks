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
