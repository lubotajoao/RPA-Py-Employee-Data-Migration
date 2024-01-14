import json

with open("config.json", "rb") as read_file:
    configFile = json.load(read_file)

application_path = (configFile['ApplicationPath'])
data_migration_portal_url = (configFile['DataMigrationPortalURL'])
api_migration_data_url = (configFile['APIMigrationDataURL'])
api_url = (configFile['api_url'])
data_migration_web_window = (configFile['data_migration_web_window'])
legacy_app_window = (configFile['legacy_app_window'])
