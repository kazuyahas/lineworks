from fastapi import Form

@router.post("/apply/{form}/submit", response_class=HTMLResponse)
async def apply_submit(form: str, request: Request):
    form_data = await request.form()

    # ★ここで Neon DB 保存 or LINE WORKS Workflow API 呼び出し
    # form_data にすべて入っている

    return f"""
    <html><body>
        <h2>{form} の申請を受け付けました</h2>
        <pre>{dict(form_data)}</pre>
    </body></html>
    """
