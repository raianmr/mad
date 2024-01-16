from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from pathlib import Path
import json

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore',
        env_file_encoding='utf-8-sig',
        case_sensitive=False,
    )

    db_host: str
    db_username: str
    db_password: str
    db_name: str
    gh_token: str
    jira_token: str


settings = Settings()

class Repo(BaseModel):
    name: str
    git_url: str
    jira_url: str

repos = [Repo(**params) for params in json.loads(Path("./repos.json").read_text())]