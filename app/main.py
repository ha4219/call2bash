import os
from fastapi import FastAPI
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_ENV: str = 'dev'
    FTP_USER: str = ''
    FTP_ADDRESS: str = ''
    FTP_PASSWORD: str = ''
    FTP_PORT: str = ''

    class Config:
        env_file = '.env'

settings = Settings()
app = FastAPI()

@app.get("/")
async def root():
    try:
        os.environ['FTP_ADDRESS'] = settings.FTP_ADDRESS
        os.environ['FTP_PORT'] = settings.FTP_PORT
        os.environ['FTP_USER'] = settings.FTP_USER
        os.environ['FTP_PASSWORD'] = settings.FTP_PASSWORD
        os.system('app/sh/build2ftp.sh')
        return 'success'
    except:
        return 'fail'