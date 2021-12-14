""" Main file for running power network models in PyENr format """

import os
import time
from pywr.model import Model
from pywr_dcopf.core import Bus, Line, Generator, Load
# from pywr.recorders import NumpyArrayNodeRecorder, NumpyArrayStorageRecorder
# from pywr.recorders import NumpyArrayNodeDeficitRecorder, AggregatedRecorder
# from pywr.parameters import *
# from demand_proj_rate_Parameter import Demand_hourly_profile
# from demand_proj_rate_Parameter import demand_proj_rate_Parameter
TEST_FOLDER = os.path.dirname(__file__)
MODEL_FILENAME = 'Myanmar_pyenr_model.json'


def timeit(func):
    def wrapper(*args, **kwargs):
        tic = time.perf_counter()
        func(*args, **kwargs)
        toc = time.perf_counter()
        print(f"Simulation time: {toc - tic:0.4f} seconds")
    return wrapper


@timeit
def run_model():
    model = Model.load(
        os.path.join(TEST_FOLDER, 'models', MODEL_FILENAME),
        solver='glpk-dcopf')
    model.setup()
    model.run()


if __name__ == "__main__":
    run_model()
