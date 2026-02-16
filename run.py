import os
import random
import subprocess
import time

seed = 42
random.seed(seed)

runs = ["true"] * 1 + ["false"] * 1
random.shuffle(runs)

for i, mixed_precision_flag in enumerate(runs):
    print(f"Run {i + 1} - Mixed precision flag: {mixed_precision_flag}", flush=True)  # flush ensures immediate output

    env = os.environ.copy()
    env["USE_MIXED_PRECISION"] = mixed_precision_flag
    env["RUN_ID"] = str(i)

    subprocess.run(
        ["jupyter", "nbconvert", "--to", "notebook", "--execute", "cifar10-with-cnn.ipynb", "--stdout"],
        env=env,
        check=True
    )

    time.sleep(120)
