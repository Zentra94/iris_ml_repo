import unittest
from mlops.train_model import train_update
from mlops.preprocess import preprocess
from data.utils import BigQueryManager
import os
from configs import PATH_DATA_MODELS

class mlopsTrainModel(unittest.TestCase):
    def test_train_update(self):
        query = """
                SELECT
                  *
                FROM
                  `tc-sc-bi-bigdata-corp-tsod-dev.gcp_learning.iris_data`;
                """
        data = BigQueryManager().read_data_gbq(query=query)
        data_t = preprocess(data=data)
        model_name = "model"
        train_update(data_t)
        self.assertEqual(os.path.isfile(PATH_DATA_MODELS / "{}.sav".format(model_name)) , True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
