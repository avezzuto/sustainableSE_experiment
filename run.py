import os
import random
import subprocess

seed = 42
random.seed(seed)

runs = ["sgd"] * 1 + ["sgd_momentum"] * 1 + ["rmsprop"] * 1 + ["adam"] * 1 + ["adamw"] * 1
random.shuffle(runs)

for i, mode in enumerate(runs):
    print(f"Run {i + 1} - Mode: {mode}", flush=True)  # flush ensures immediate output

    env = os.environ.copy()
    env["OPTIMIZER"] = mode
    env["RUN_ID"] = str(i)

    subprocess.run(
        ["jupyter", "nbconvert", "--to", "notebook", "--execute", "cifar10-with-cnn.ipynb", "--stdout"],
        env=env,
        check=True
    )
