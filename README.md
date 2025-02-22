# JotForm Notifier

## Introduction

JotForm Notifier returns notifications to channels in telex when forms have been filled.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/01kazu/telex-jotform.git
cd telex-jotform
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the server:

```bash
uvicorn main:app
```

## API Endpoints
- `POST /ap1/v1/jotform-notify/"channel_id"` - sends notifications to designated telex channels
- `GET /api/v1/integration.json` - used to any integration on telex

## Running Tests

```bash
pytest
```

## Error Handling

The API includes proper error handling for:

- Wrong form title key from the Request object
- Failed Notifications


## USAGE
### How to connect this API to JotForm

1. Click on **Create Form** or **Edit Form**
![Step 1 image](images/step_1.png)


2. Click on **Settings**
![Step 2 image](images/step_2.png)


3. Click on **Integrations**
![Step 3 image](images/step_3.png) 


4. On the Search bar, type in "webhook"
![Step 4 image](images/step_4.png)


5. In the Add WebHook input, paste "https://telex-jotform.onrender.com/jotform/"
![Step 5 image](images/step_5.png)


6. To get your channel_id, click on a channel and copy the series of words and numbers
![Step 8 image](images/step_6.png)


7. Then paste it, after "/" such that it would be arranged in the format "https://telex-jotform.onrender.com/jotform/01952380-317f-7921-b16b-17c82d79e827"
![Step 8 image](images/step_7.png)


8. Click on **Complete Integration**
![Step 8 image](images/step_8.png)


9. Congratulations!!!
![Step 9 image](images/step_9.png)


10. When a form is submitted.
![Step 10 image](images/step_10.png)


11. The title of the form is sent as a notification
![Step 11 image](images/step_11.png)







