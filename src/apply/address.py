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
