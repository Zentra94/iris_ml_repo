import unittest
from mlops.preprocess import preprocess
from data.utils import BigQueryManager, show_data_frame_as_tabulate


class mlopsPreprocess(unittest.TestCase):
    def test_preprocess(self):
        query = """
        SELECT
          *
        FROM
          `tc-sc-bi-bigdata-corp-tsod-dev.gcp_learning.iris_data`;
        """
        data = BigQueryManager().read_data_gbq(query=query)

        data_t = preprocess(data=data)
        show_data_frame_as_tabulate(data_t, show_first=10)

        for i in range(0, 3):
            self.assertEqual(i in data_t["target"].unique(), True)


if __name__ == '__main__':
    unittest.main()
