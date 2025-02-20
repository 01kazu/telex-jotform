import httpx
from fastapi import Request, status, APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


# @router.post("/jotform")
# async def jotform(request: Request):
#     try:
#         # Remind the user to make sure channel ID is in the settings
#         body = await request.json()

#         channel_id = body.get("settings")[0].get("default")
#         print(channel_id)
#         command = body.get("message")
#         if command is None:
#             telex_format = {
#                 "event_name": "Invalid Command",
#                 "message": f'Enter "/start" to activate JotForm Bot',
#                 "status": "error",
#                 "username": "JotForm Bot"
#             }
#             await send_message(channel_id, telex_format)
#             return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST, 
#                                 content = {"response": "Invalid command"})
        
#         command = command.strip().replace("<p>", "").replace("</p>", "")

#         if command == "/start":
#             jotform_url = f"https://telex-jotform.onrender.com/api/v1/jotform/{channel_id}" # Put API URL in settings
#             telex_format = {
#                 "event_name": "Copy this url to your JotForm Webhook",
#                 "message": f"{jotform_url}",
#                 "status": "success",
#                 "username": "JotForm Bot"
#             }
#             await send_message(channel_id, telex_format)
#             return JSONResponse(status_code = status.HTTP_200_OK, 
#                                 content = {"response": "JotForm Bot has been activated"})
#         else:
#             telex_format = {
#                 "event_name": "Invalid Command",
#                 "message": f'Enter "/start" to activate JotForm Bot',
#                 "status": "error",
#                 "username": "JotForm Bot"
#             }
#             await send_message(channel_id, telex_format)
#             return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST, 
#                                 content = {"response": "Invalid command"})
#     except Exception as e:
#         print(f"Failed | error: {e}")
#         return {"status": "error", "message": str(e), "status": "error"}

    
@router.get("/jotform/{channel_id}")
async def jotform(request: Request, channel_id: str):
    try:
        # if form_data is None return 
        body = await request.body()

        form_data = await request.form()
        form_title = form_data.get("formTitle")

        # Find a way to get the channel webhook URL form telex
        # url = f"https://ping.telex.im/v1/webhooks/{0195181a-e640-7f85-a0c6-d32f46804380}"
        telex_format = {
            "event_name": "Form Sent",
            "message": f"{form_title} has been filled",
            "status": "success",
            "username": "JotForm Bot"
        }
        await send_message(channel_id, telex_format)
        return JSONResponse(status_code = status.HTTP_200_OK, 
                        content = {"response": f"{form_title} form has been filled"})
    except Exception as e:
        print(f"Failed | error: {e}")
        return {"status": "error", "message": str(e)}
    

async def send_message(channel_id: str, telex_format: dict):
    channel_webhook_url = f"https://ping.telex.im/v1/webhooks/{channel_id}" # Put ping telex in settings
    async with httpx.AsyncClient() as client:
        response = await client.post(channel_webhook_url, json=telex_format)
        response.raise_for_status()


@router.post("/jotform")
async def jotform(request: Request):
    await body = request.json()
    return {"status": "success", "message": "Test Passed Successfully"}