from pydantic import BaseSettings
from typing import Optional
import secrets

class Settings(BaseSettings):
    """ Configurações globais """

    API_V1: str = "/api/v1"
    ENV_STATE : Optional[str]

    DATABASE_URL: Optional[str] = None

    class Config:
        
        env_file = ".env"


class DevSettings(Settings):
    """ Configurações de Desenvolvimento"""

    class Config:
        env_prefix: str = "DEV_"


class TestSettings(Settings):
    """ Configurações de Teste"""

    class Config:
        env_prefix: str = "TEST_"


class ProdSettings(Settings):
    """ Configurações de Produção """

    class Config:
        env_prefix: str = "PROD_"


class FactorySettings:
    """ Retorna uma instância do Settings dependendo do ENV_STATE """

    def __init__(self, env_state: str):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "dev":
            return DevSettings()

        elif self.env_state == "test":
            return TestSettings()

        elif self.env_state == "prod":
            return ProdSettings()
        else:
            raise Exception("Defina o ENV_STATE no arquivo .env como test, dev ou prod")


settings = FactorySettings(Settings().ENV_STATE)()
