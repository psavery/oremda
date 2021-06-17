import numpy as np

from oremda import Client as OremdaClient
from oremda import Pipeline as OremdaPipeline
from oremda.constants import DEFAULT_PLASMA_SOCKET_PATH
from oremda.utils.plasma import start_plasma_store

kwargs = {
    'memory': 50000000,
    'socket_path': DEFAULT_PLASMA_SOCKET_PATH,
}

with start_plasma_store(**kwargs):
    client = OremdaClient(DEFAULT_PLASMA_SOCKET_PATH)
    pipeline = OremdaPipeline(client)

    operators = [
        {
            "name": "eels_background_subtract",
            "params": {
                "start": 268,
                "stop": 277,
            }
        },
    ]

    data = np.array([5, 9, 2, 3, 8, 10], dtype=np.int16)

    output_data = pipeline.run(operators, data)
