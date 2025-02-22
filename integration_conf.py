from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()



@router.get("/integration.json")
def get_integration_json(request: Request):
    base_url = str(request.base_url).rstrip("/")

    integration_json = {
      "data": {
        "date": {
          "created_at": "2025-02-20",
          "updated_at": "2025-02-20"
        },
        "descriptions": {
          "app_name": "JotForm Notifier",
          "app_description": "This integration gives notifications when forms are filled on Jotform.",
          "app_logo": "https://imgur.com/a/2T8DDoL",
          "app_url": base_url,
          "background_color": "#fff"
        },
        "is_active": False,
        "integration_type": "modifier",
        "integration_category": "Monitoring & Logging",
        "key_features": [
          "Notifications"
        ],
        "author": "Joshua Yakubu David",
        "website": base_url,
        "settings": [
          {
            "label": "Channel ID",
            "type": "text",
            "required": True,
            "default": "Channel ID"
          }
        ],
      }
    }
    return JSONResponse(content=integration_json)
