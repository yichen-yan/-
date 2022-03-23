from math import exp
import pandas as pd


def get_resource(csv_path):
    """
    获取原始数据
    :param csv_path:csv原始数据路径
    :return:frame
    """
    frame = pd.read_csv(csv_path)
    return frame


def predict_all(records, user_cluster, item_cluster):
    """

    :param records:
    :param user_cluster:
    :param item_cluster:
    :return:
    """


class Cluster:
    def __init__(self, records):
        self.group = dict()

    def get_group(self, i):
        return 0

class IdCluster()

