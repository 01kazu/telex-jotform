import requests
import httpx
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from integration_conf import router as integration_router
from config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(integration_router, prefix=settings.API_PREFIX)

@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.post("/jotform")
async def jotform(request: Request):
    try:
        # Conditional Statement to check if request has form data
        form_data = await request.form()
        form_title = form_data.get("formTitle")
        print(form_title)
        # Find a way to get the channel webhook URL form telex
        url = "https://ping.telex.im/v1/webhooks/0195181a-e640-7f85-a0c6-d32f46804380"
        payload = {
            "event_name": "Form Sent",
            "message": f"{form_title} has been filled",
            "status": "success",
            "username": "JotForm Bot"
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
        # telex_response = notifications(url, payload)
    except Exception as e:
        print(f"Failed | error: {e}")
        return {"status": "error", "message": str(e)}
    return JSONResponse(status_code = status.HTTP_200_OK, 
                        content = {"response": "Form has been filled by User2",
                                   "telex_response": telex_response})


def notifications(url, payload):
    response = requests.post(
                    url,
                    json=payload,
                    headers={
                        "Accept": "application/json",
                        "Content-Type": "application/json"
                    }
                )
    return response.json()
