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
- `POST /jotform` - sends notifications to designated telex channels
- `GET /api/v1/integration.json` - used to any integration on telex

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

5. In the Add WebHook input, paste "https://telex-jotform.onrender.com/jotform"
![Step 5 image](images/step_5.png)

6. Click on **Complete Integration**
![Step 6 image](images/step_6.png)

7. Congratulations!!!
![Step 7 image](images/step_7.png)






