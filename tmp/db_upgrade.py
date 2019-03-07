from migrate.versioning import api
from config import Config

def Upgrade():
    api.upgrade(Config.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO)
    v = api.db_version(Config.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO)
    print("Current db version ", str(v))

def Downgrade():
    v = api.db_version(Config.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO)
    api.downgrade(Config.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO, v-1)
    v = api.db_version(Config.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO)
    print("Current db version", v)


if __name__ == "__main__":
    Upgrade()