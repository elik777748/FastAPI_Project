from pydantic_settings import BaseSettings


class DataBaseSettings(BaseSettings):
    PGHOST: str
    PGDATABASE: str
    PGUSER: str
    PGPASSWORD: str
    PGPORT: int = 5432

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://neondb_owner://{self.PGUSER}:{self.PGPASSWORD}@{self.PGHOST}:{self.PGPORT}/{self.PGDATABASE}"

class Settings(DataBaseSettings):
    DEBUG: bool = False


settings = Settings()
