from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()


integration_json = {
  "data": {
    "date": {
      "created_at": "2025-02-19",
      "updated_at": "2025-02-19"
    },
    "descriptions": {
      "app_name": "JotForm Notifier",
      "app_description": "This integration gives notifications when forms are filled on Jotform.",
      "app_logo": "https://telex-jotform.onrender.com/logo",
      "app_url": "https://telex-jotform.onrender.com",
      "background_color": "#fff"
    },
    "is_active": True,
    "integration_type": "modifier",
    "integration_category": "Monitoring & Logging",
    "key_features": [
      "Notifications"
    ],
    "author": "Joshua Yakubu David",
    "settings": [
      {
        "label": "Channel ID",
        "type": "text",
        "required": True,
        "default": "Channel ID"
      }
    ],
    "target_url": "https://telex-jotform.onrender.com/api/v1/integration",
    "tick_url": "https://telex-jotform.onrender.com/api/v1/tick"
  }
}


@router.get("/integration.json")
async def get_integration_json():
    return JSONResponse(content=integration_json)


@router.get("/integration")
async def integration(request: Request):
    try:
        payload = await request.json()
        print(payload)
        return {'payload': "payload recieved"}
    except Exception as e:
        print(f"Failed | error: {e}")
        return {"status": "error", "message": str(e)}