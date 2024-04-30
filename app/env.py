import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())


def _getenv(key: str):
    env = os.getenv(key)
    if env is None:
        return env

    # 空文字列の場合はNoneを返す
    if env.strip() == "":
        os.environ.pop(key)
        return None

    return env


def _getenv_or_default(key, default):
    env = _getenv(key)
    if env is None:
        return default
    return env


class Env:
    # アプリケーション関連
    TEST = _getenv_or_default("TEST", "default")
    APP_NAME = _getenv_or_default("APP_NAME", "sass-arsaga-insight-engine")
    DATABASE_HOST = _getenv("DATABASE_HOST")
    DATABASE_NAME = _getenv("DATABASE_NAME")
    DATABASE_USER = _getenv("DATABASE_USER")
    DATABASE_PASSWORD = _getenv("DATABASE_PASSWORD")
    DATABASE_PORT = _getenv("DATABASE_PORT")
