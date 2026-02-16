import os
import random
import subprocess
import time

seed = 42
random.seed(seed)

runs = ["true"] * 10 + ["false"] * 10
random.shuffle(runs)

warmup_duration_seconds = 300 # 5 minute CPU warm-up

print(f"Starting CPU warm-up for {warmup_duration_seconds} seconds...", flush=True)

start_time = time.time()

# Iterative Fibonacci
a, b = 0, 1
while time.time() - start_time < warmup_duration_seconds:
    a, b = b, a + b
    if a > 10 ** 1000:
        a, b = 0, 1

print("CPU warm-up completed.\n", flush=True)

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
