import requests
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.post("/jotform")
async def jotform(request: Request):
    try:
        print(f"Info | Step 1: Achieved")
        form_data = await request.form()
        print(f"Info | Step 2: Achieved")
        print(form_data)
        # Find a way to get the channel webhook URL form telex
        url = "https://ping.telex.im/v1/webhooks/0195181a-e640-7f85-a0c6-d32f46804380"
        payload = {
            "event_name": "Form Sent",
            "message": "Form has been filled by User2",
            "status": "success",
            "username": "JotForm Bot"
        }
        telex_response = notifications(url, payload)
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
