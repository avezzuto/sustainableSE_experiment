import os
import random
import subprocess

seed = 42
random.seed(seed)

runs = ["cpu"] * 1 + ["gpu"] * 1
random.shuffle(runs)

for i, mode in enumerate(runs):
    print(f"Run {i + 1} - Mode: {mode}", flush=True)  # flush ensures immediate output

    env = os.environ.copy()
    env["RUN_MODE"] = mode

    subprocess.run(
        ["jupyter", "nbconvert", "--to", "notebook", "--execute", "mnist-cnn-classification.ipynb", "--stdout"],
        env=env,
        check=True
    )
