from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg2://task_api:task_api@localhost:5432/task_api"
    model_config = {"env_file": ".env"}

settings = Settings()

