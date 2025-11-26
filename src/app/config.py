from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    whisker_username: str
    whisker_password: str
    doorbell_url: str
    doorbell_username: str
    doorbell_password: str
    ha_token: str
    ha_url: str
    scrypted_url: str
    ha_entities_url: str


__settings = None


def settings() -> Settings:
    global __settings
    if not __settings:
        __settings = Settings()
    return __settings
