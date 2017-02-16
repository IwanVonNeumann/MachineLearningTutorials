import numpy as np

DATA_PATH = "data/pima-indians-diabetes.data"


def get_data():
    return np.loadtxt(DATA_PATH, delimiter=",")
