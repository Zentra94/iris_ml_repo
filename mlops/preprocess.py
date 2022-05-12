from data.utils import get_dict


def preprocess(data):
    data_t = data.copy()
    label_enc = get_dict("target_labels.json")
    data_t["target"] = data_t["target"].apply(lambda x: label_enc[x])
    return data_t
