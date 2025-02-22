import asyncio
import requests
import httpx
from fastapi import Request, APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()
# how would i know the channel id is correct

    
@router.post("/jotform-notify/{channel_id}")
async def jotform_notify(request: Request, channel_id: str):
    try:
        form_data = await request.form()
        form_title = form_data.get("formTitle") # Testing point: Logging
        if form_title:
            telex_format = {
                "event_name": "Form Sent",
                "message": f"{form_title} has been filled",
                "status": "success",
                "username": "JotForm Bot"
            }
            response = send_message(channel_id, telex_format)
            return JSONResponse(status_code = status.HTTP_200_OK, content = response)
    except Exception as e:
        print(f"Failed | error: {e}") # Add logging
        return {"status": "error", "message": str(e)}
    

async def send_message(channel_id: str, telex_format: dict):
    telex_webhook_url = f"https://ping.telex.im/v1/webhooks/{channel_id}" # Put ping telex in settings
    async with httpx.AsyncClient() as client:
        response = await client.post(
                telex_webhook_url, json=telex_format, headers={"Content-Type": "application/json"}
            )

    