import asyncio
from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
app.mount("/assets", StaticFiles(directory="resources/assets"), name="assets")

templates = Jinja2Templates(directory="resources")


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/overlay", response_class=HTMLResponse)
async def overlay_base(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, }
    )


def main() -> None:
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, loop="asyncio")
    server = uvicorn.Server(config)

    asyncio.run(server.serve())


if __name__ == "__main__":
    main()
