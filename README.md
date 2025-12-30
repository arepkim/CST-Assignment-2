# Parallel Image Processing on Google Cloud Platform

## Project Overview
This project implements a parallel image processing system that applies multiple image filters to a subset of the Food-101 dataset. The same image processing pipeline is implemented using different parallel programming paradigms in Python and deployed on Google Cloud Platform (GCP) to analyze performance characteristics such as execution time, speedup, and efficiency.

The image processing pipeline includes:
1. Grayscale conversion
2. Gaussian blur (3×3 kernel)
3. Sobel edge detection
4. Image sharpening
5. Brightness adjustment

Each image is processed independently, making the problem suitable for data-level parallelism.

---

## Parallel Programming Paradigms Used
This project implements the pipeline using the following approaches:
- **Sequential execution** (baseline)
- **Multiprocessing** using Python `multiprocessing.Pool`
- **Task-based parallelism** using `concurrent.futures.ProcessPoolExecutor`

---

## Dataset
The Food-101 dataset is used:
https://www.kaggle.com/datasets/dansbecker/food-101

Only a manageable subset of images is used for testing and benchmarking to ensure reasonable execution time.

Dataset structure:
data/
├── cup_cakes/
├── pizza/
└── sushi/

How to Run (Local Machine)
1. Sequential Execution
python sequential.py

2. Multiprocessing Version
python multiprocessing_version.py

3. concurrent.futures Version
python futures_version.py

Performance Evaluation

Performance is evaluated using:

Execution Time

Speedup

Efficiency

Speedup is calculated as:

Speedup = T_sequential / T_parallel


Efficiency is calculated as:

Efficiency = Speedup / Number_of_Workers


All measurements are taken using the same dataset and execution environment to ensure fair comparison.

Output

Processed images are saved to separate output folders for each implementation:

output_sequential/
output_multiprocessing/
output_futures/