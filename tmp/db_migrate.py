import imp
import os
from migrate.versioning import api
from app import db
from config import Config

v = api.db_version(Config.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO)
sPath = os.path.join(Config.SQLALCHEMY_MIGRATE_REPO, "versions")
migration = os.path.join(sPath, "%03d_migration.py" %(v+1))
tmp_module = imp.new_module("old_model")
old_model = api.create_model(Config.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO)
exec(old_model, tmp_module.__dict__)
script = api.make_update_script_for_model(Config.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO,
                                          tmp_module.meta, db.metadata)
with open(migration, "w") as f:
    f.write(script)

api.upgrade(Config.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(Config.SQLALCHEMY_DATABASE_URI, Config.SQLALCHEMY_MIGRATE_REPO)
print("New migration save as ", migration)
print("New verions is", v)

