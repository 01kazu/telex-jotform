import pytest
from webhook import send_message


@pytest.mark.asyncio
async def test_send_message():
    response = await send_message(channel_id="01951814-03cf-7f85-a688-63ba80b05b48", 
                           telex_format={"event_name": "Form Sent - Notify", 
                                        "message": "Form has been filled", 
                                        "status": "success", 
                                        "username": "JotForm Notifier"})
    assert response.status_code == 202
    data = response.json()
    assert data["status"] == "success"
    assert data["message"] == "request received"

