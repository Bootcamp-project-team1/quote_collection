from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):

    # 비동기 DB URL
    database_url: str = Field(..., alias="DATABASE_URL")

    # 동기 DB URL
    sync_database_url: str = Field(..., alias="SYNC_DATABASE_URL")

    secret_key: str = Field(..., alias="SECRET_KEY")
    jwt_algo: str = Field("HS256", alias="ALGORITHM")
    access_token_expire_minutes: int = Field(
        30, alias="ACCESS_TOKEN_EXPIRE_MINUTES"
    )  # 30분

    class Config:
        case_sensitive = True
        extra = "allow"
        populate_by_name = True
        # env_file = ".env"
        env_file = ".env.dev"  # 개발 도중에는 이걸 사용 (배포할떄 바꾸기)


settings = Settings()
