from pathlib import Path
import os
from dotenv import load_dotenv

PATH_MAIN = Path(os.path.dirname(__file__))
PATH_DATA = PATH_MAIN / "data"
PATH_DATA_DICTS = PATH_DATA / "dicts"
PATH_DATA_MODELS = PATH_DATA / "models"
PATH_TABLES = PATH_DATA / "tables"
PATH_MLOPS = PATH_MAIN / "mlops"
PATH_TEST = PATH_MAIN / "tests"
PATH_STATICS = PATH_MAIN / "statics"

load_dotenv()
GCP_CRED_PATH = os.getenv("GCP_CRED_PATH")
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")

if __name__ == '__main__':
    print("the main path is: {}".format(PATH_MAIN))
    vars = locals().copy()
    paths = {}
    for k, v in vars.items():
        if k.startswith("PATH_"):
            path = Path(v)
            if path.is_dir():
                print("directory {} already exists".format(v))
            else:
                os.mkdir(path)
                print("directory {} created".format(v))
