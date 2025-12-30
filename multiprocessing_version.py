import os
import time
import argparse
from multiprocessing import Pool
from pipeline import process_image
from utils import get_image_paths

INPUT_DIR = "data"
OUTPUT_DIR = "output_multiprocessing"
WORKER_COUNTS = [2, 4, 8]

def worker(img_path):
    rel_path = os.path.relpath(img_path, INPUT_DIR)
    output_path = os.path.join(OUTPUT_DIR, rel_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    process_image(img_path, output_path)

def run_with_workers(num_workers, image_paths, sequential_time=None):
    print(f"Running with {num_workers} processes...")
    start = time.time()
    with Pool(processes=num_workers) as pool:
        pool.map(worker, image_paths)
    end = time.time()
    duration = end - start
    print(f"Multiprocessing Time ({num_workers} processes): {duration:.2f} seconds")

    if sequential_time:
        speedup = sequential_time / duration
        efficiency = speedup / num_workers
        print(f"  Speedup: {speedup:.2f}x")
        print(f"  Efficiency: {efficiency:.2f}")

def main():
    parser = argparse.ArgumentParser(description="Run multiprocessing image processing.")
    parser.add_argument("--seq_time", type=float, help="Execution time of the sequential version for performance analysis", default=None)
    args = parser.parse_args()

    image_paths = get_image_paths(INPUT_DIR)

    for num_workers in WORKER_COUNTS:
        run_with_workers(num_workers, image_paths, args.seq_time)

if __name__ == "__main__":
    main()
