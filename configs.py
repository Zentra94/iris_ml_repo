from pathlib import Path
import os

PATH_MAIN = Path(os.path.dirname(__file__))
PATH_DATA = PATH_MAIN / "data"
PATH_DATA_DICTS = PATH_DATA / "dicts"
PATH_DATA_MODELS = PATH_DATA / "models"
PATH_TABLES = PATH_DATA / "tables"
PATH_MLOPS = PATH_MAIN / "mlops"
PATH_TEST = PATH_MAIN / "tests"

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
