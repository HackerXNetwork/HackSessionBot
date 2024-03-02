class Config:
    API_ID = 
    API_HASH = ""
    TOKEN = ""  
    START_PIC = "" 
    CHAT = ""    
  "addons": [],
    "buildpacks": [
        {
            "url": "heroku/python"
        }
    ],
    "formation": {
        "worker": {
            "quantity": 1,
            "size": "free"
        }
    }
