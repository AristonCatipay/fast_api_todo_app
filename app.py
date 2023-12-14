from fastapi import FastAPI, Depends, Request, Form, status

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/")
def read(request: Request, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).all()
    return templates.TemplateResponse("base.html",
                                      {"request": request, "todo_list": todo})