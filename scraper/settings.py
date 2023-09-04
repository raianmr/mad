from pydantic_settings import BaseSettings, SettingsConfigDict


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


settings = Settings()
