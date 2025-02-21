import requests
from fastapi import Request, APIRouter

router = APIRouter()

    
@router.post("/jotform-notify/{channel_id}")
async def jotform_notify(request: Request, channel_id: str):
    try:
        form_data = await request.form()
        form_title = form_data.get("formTitle")
        telex_format = {
            "event_name": "Form Sent",
            "message": f"{form_title} has been filled",
            "status": "success",
            "username": "JotForm Bot"
        }
        send_message(channel_id, telex_format)
    except Exception as e:
        print(f"Failed | error: {e}") # Add logging
        return {"status": "error", "message": str(e)}
    

def send_message(channel_id: str, telex_format: dict):
    telex_webhook_url = f"https://ping.telex.im/v1/webhooks/{channel_id}" # Put ping telex in settings
    response = requests.post(telex_webhook_url, 
                                json=telex_format,
                                headers={"Content-Type": "application/json"})

 