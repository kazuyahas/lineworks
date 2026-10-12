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
