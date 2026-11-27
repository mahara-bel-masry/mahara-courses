import os
def get_config():
    return {
        "env": os.environ.get("APP_ENV", "local"),
        "path": os.environ.get("DATA_PATH", "/tmp/data"),
    }
print(get_config())
os.environ["APP_ENV"] = "cloud"
os.environ["DATA_PATH"] = "container/data"
print(get_config())
