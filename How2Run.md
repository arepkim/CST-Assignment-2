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