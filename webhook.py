import asyncio
import httpx
from fastapi import Request, APIRouter
from fastapi.responses import JSONResponse

from config import settings

router = APIRouter()


@router.post("/jotform-notify/{channel_id}")
async def jotform_notify(request: Request, channel_id: str):
    try:
        form_data = await request.form()
        form_title = form_data.get("formTitle")
        if form_title:
            telex_format = {
                "event_name": "Form Sent",
                "message": f"{form_title} has been filled",
                "status": "success",
                "username": "JotForm Notifier"
            }
            response = await send_message(channel_id, telex_format)
            if 200 <= response.status_code < 400:
                print("message sent successfully")
                return {"status": "success", "message": "Message sent successfully"}
            print("Failed to send message")
            return JSONResponse(status_code=404, 
                                content={"status": "error", "message": "Failed to send message"})
        print("form title not found")
        return JSONResponse(status_code=404, 
                            content = {"status": "error", "message": "form title not found"})
    except Exception as e:
        print(f"Failed | error: {e}")
        return {"status": "error", "message": str(e)}
    

async def send_message(channel_id: str, telex_format: dict):
    telex_webhook_url = f"{settings.TELEX_WEBHOOK}/{channel_id}"
    print(telex_webhook_url)
    async with httpx.AsyncClient() as client:
        response = await client.post(
                telex_webhook_url, json=telex_format, 
                headers={"Content-Type": "application/json"}
            )
        return response