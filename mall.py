from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory=".")

users = {
    "lesheng": {
        "name": "lesheng",
        "stores": []
    },
    "laoxu": {
        "name": "laoxu",
        "stores": []
    },
}


@app.get("/")
def read_root():
    with open('pages/mall.html', 'r') as file:
        content = file.read()
    return HTMLResponse(content)


@app.get("/{user_id}", response_class=HTMLResponse)
def read_user(request: Request, user_id):
    user = users.get(user_id)
    if user:
        return templates.TemplateResponse("pages/user.html", {"request": request, "user": user})
    else:
        raise HTTPException(status_code=404)
