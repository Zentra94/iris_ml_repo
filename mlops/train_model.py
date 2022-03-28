from configs import PATH_DATA_MODELS, PATH_DATA_DICTS
from sklearn import svm
import joblib

def train_update(data, target="target", model_name="model"):
    features = [c for c in data.columns if c != target]
    model = svm.SVC()
    model.fit(X=data[features], y=data[target])
    joblib.dump(model, PATH_DATA_MODELS / "{}.sav".format(model_name))

