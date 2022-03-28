import unittest
from data.utils import (example_operation, BigQueryManager, show_data_frame_as_tabulate)


class dataUtils(unittest.TestCase):
    def test_example_operation(self):
        tests = [(1, 1, 1), (2, 1, -1), (1, 3, 6)]
        for t in tests:
            x = t[0]
            y = t[1]
            exp_res = t[2]
            res = example_operation(x=x, y=y)
            self.assertEqual(res, exp_res)

    def test_BigQueryManager(self):
        query = """
        SELECT
          *
        FROM
          `tc-sc-bi-bigdata-corp-tsod-dev.gcp_learning.iris_data` LIMIT 10;
        """
        bqm = BigQueryManager()
        data = bqm.read_data_gbq(query=query)
        show_data_frame_as_tabulate(data)
        self.assertEqual(len(data), 10)

if __name__ == '__main__':
    unittest.main()
