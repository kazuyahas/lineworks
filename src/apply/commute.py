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
