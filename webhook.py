import httpx
from fastapi import Request, status, APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/jotform")
async def jotform(request: Request):
    try:
        # if form_data is None return 
        body = await request.body()
        print(body)

        form_data = await request.form()
        form_title = form_data.get("formTitle")

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
        return JSONResponse(status_code = status.HTTP_200_OK, 
                        content = {"response": f"{form_title} form has been filled"})
    except Exception as e:
        print(f"Failed | error: {e}")
        return {"status": "error", "message": str(e)}