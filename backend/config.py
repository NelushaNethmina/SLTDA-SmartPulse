from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    #data_base settings
    db_url: str = ("postgresql://postgres:SLTDA%40SmartPulse"
        "%232026!@localhost:5432/sltda_smartpulse")
    db_host: str = "localhost"
    db_port: str = "5432"
    db_name: str = "sltda_smartpulse"
    db_user: str = "postgres"
    db_password: str = "SLTDA@SmartPulse#2026!"

    #security settings
    secret_key: str = "SmartPulse@JWT#2026!SLTDA$Secure"
    algorithm: str = "HS256"
    token_expire_minutes: int = 60

    #external api settings
    claude_api_key: str = ""
    amadeus_api_key: str = ""
    amadeus_api_secret: str = ""


    #application settings
    app_name: str = "SLTDA SmartPulse"
    debug: bool = False
    

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()