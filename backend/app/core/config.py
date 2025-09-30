from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    
    # 비동기 DB URL
    database_url: str = "mysql+aiomysql://root:12345@127.0.0.1:3306/quote_collection?charset=utf8mb4"

    # 동기 DB URL
    sync_database_url: str = "mysql+pymysql://root:12345@127.0.0.1:3306/quote_collection?charset=utf8mb4"

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
