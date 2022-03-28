import json
from google.cloud import bigquery
from google.oauth2 import service_account
from configs import PATH_DATA_DICTS, PATH_MAIN, GCP_CRED_PATH, GCP_PROJECT_ID
from tabulate import tabulate

def get_dict(dict_name):
    path = PATH_DATA_DICTS / dict_name
    if path.is_file():
        with open(path) as json_file:
            return json.load(json_file)
    else:
        print("File {} doesn't exists".format(path))
    return {}



def show_data_frame_as_tabulate(data_frame, show_first=2000, float_decimals=-1):
    """
    Show a pd.DataFrame in a nice way
    :param float_decimals: number of decimal to print
    :type  float_decimals: int
    :param data_frame: table to be showed
    :type data_frame: pd.DataFrame
    :param show_first: number of first rows to be showed
    :type show_first: int
    """
    max_rows = min(len(data_frame), show_first)
    n_rows, n_cols = data_frame.shape

    if float_decimals >= 0:
        tabulate_table = tabulate(data_frame.iloc[0:max_rows], headers="keys", tablefmt="psql", floatfmt=".{}f".format(float_decimals), missingval="?", numalign="right")
    else:
        tabulate_table = tabulate(data_frame.iloc[0:max_rows], headers="keys", tablefmt="psql", missingval="?", numalign="right")
    print("Showing {}/{} rows and {} columns".format(max_rows, n_rows, n_cols))
    print(tabulate_table)

def example_operation(x, y):
    """
    sandbox operation: sum numbers between x and y (x<y)
    :param x: number 1
    :type x: int
    :param y: int
    :type y: number 2
    :return: result of operation
    :rtype: int
    """
    res = 0
    if x > y:
        return -1
    for i in range(x, y+1):
        res += i
    return res

class BigQueryManager:
    def __init__(self, project=GCP_PROJECT_ID, cred_path=PATH_MAIN / GCP_CRED_PATH):
        credentials = service_account.Credentials.from_service_account_file(cred_path)
        self.client = bigquery.Client(location="US", project=project, credentials=credentials)

    def load_data_gbq(self, data, table_name, data_set, replace=False):
        n = len(data)
        dataset = self.client.get_dataset(data_set)
        table_ref = dataset.table(table_name)
        job_config = bigquery.job.LoadJobConfig()
        if replace:
            job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
        job = self.client.load_table_from_dataframe(data, table_ref, location="US", job_config=job_config)
        job.result()
        print("Loaded dataframe with {} rows to {}".format(n, table_ref.path))

    def read_data_gbq(self, query):
        query_fmt = "".join([c for c in query if c.isnumeric() or c.isalpha()])
        query_fmt_lmts = min(15, int(len(query_fmt) * 0.25))
        print("Executing query {} ... {}".format(query[:query_fmt_lmts], query[-query_fmt_lmts:]))
        query_job = self.client.query(
            query,
            location="US")
        df = query_job.to_dataframe()
        print("Total rows fetched:", len(df))
        return df


