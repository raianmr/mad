from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore',
        env_file_encoding='utf-8-sig',
        case_sensitive=False,
    )

    DB_TYPE: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_HOST: str
    MAD20_LOCATION: str


settings = Settings()
