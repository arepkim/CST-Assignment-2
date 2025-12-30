# Google Cloud Platform (GCP) VM Setup Guide

This guide outlines the steps to set up a Virtual Machine (VM) on Google Cloud Platform to run your parallel image processing assignment.

## Prerequisites
*   A Google Cloud Platform account.
*   A project created in the GCP Console.

---

## Step 1: Create a VM Instance

1.  Go to the **Google Cloud Console** (https://console.cloud.google.com).
2.  In the navigation menu, go to **Compute Engine** > **VM instances**.
3.  Click **CREATE INSTANCE**.
4.  **Name:** Give your VM a name (e.g., `image-processing-vm`).
5.  **Region/Zone:** Choose a region close to you (e.g., `us-central1-a`).
6.  **Machine Configuration:**
    *   **Series:** E2
    *   **Machine type:** **Standard** -> `e2-standard-8` (8 vCPU, 32 GB memory).
    *   *Note: Since you are benchmarking up to 8 workers, you need a machine with at least 8 vCPUs to see the true benefits of parallelism. Using a smaller machine will bottleneck the performance.*
7.  **Boot Disk:**
    *   Click **Change**.
    *   Select **Operating System:** `Ubuntu`.
    *   **Version:** `Ubuntu 22.04 LTS` (or 20.04 LTS).
    *   **Size:** The default (10 GB) is usually sufficient, but 20 GB is safer.
    *   Click **Select**.
8.  **Firewall:** Check "Allow HTTP traffic" and "Allow HTTPS traffic" (optional, but good practice).
9.  Click **CREATE**.

---

## Step 2: Connect to the VM

1.  Wait for the instance status to turn green (Running).
2.  Click the **SSH** button in the "Connect" column next to your VM instance.
3.  A new browser window will open with a terminal connected to your VM.

---

## Step 3: Set Up the Environment

Run the following commands in the SSH terminal to update the system and install necessary system dependencies.

```bash
# Update package lists
sudo apt-get update

# Install pip (Python package manager)
sudo apt-get install -y python3-pip

# Install system libraries required by OpenCV (CRITICAL STEP)
# Without this, cv2 will fail to import
sudo apt-get install -y libgl1-mesa-glx libglib2.0-0
```

---

## Step 4: Upload Your Project Files

Since your files are on your local machine, the easiest way to transfer them is by zipping them first.

**On your LOCAL machine:**
1.  Select all your project files (`.py` files, `requirements.txt`, and the `data` folder).
2.  Right-click and compress them into a file named `project_files.zip`.

**In the GCP SSH Window:**
1.  Click the **Gear icon** (Settings) in the top-right corner of the SSH window.
2.  Select **Upload file**.
3.  Choose your `project_files.zip` from your computer.
4.  Wait for the upload to finish.

**Unzip the files:**
```bash
# Install unzip tool
sudo apt-get install -y unzip

# Unzip the project
unzip project_files.zip -d image_processing_project

# Enter the directory
cd image_processing_project
```

---

## Step 5: Install Python Dependencies

Run the following command to install the libraries listed in your `requirements.txt` (mainly `opencv-python` and `numpy`).

```bash
pip3 install -r requirements.txt
```

---

## Step 6: Run the Experiments

Now you can run your scripts just like you did locally.

**1. Run Sequential (Baseline)**
```bash
python3 sequential.py
```
*Note down the execution time (e.g., 6.66 seconds).*

**2. Run Multiprocessing**
Replace `[TIME]` with the time you recorded from the sequential run.
```bash
python3 multiprocessing_version.py --seq_time [TIME]
```

**3. Run Futures**
Replace `[TIME]` with the time you recorded from the sequential run.
```bash
python3 futures_version.py --seq_time [TIME]
```

---

## Step 7: (Optional) Download Results

If you want to view the output images locally:

1.  **Zip the output folders:**
    ```bash
    zip -r outputs.zip output_sequential output_multiprocessing output_futures
    ```
2.  **Download the zip:**
    *   Click the **Gear icon** in the SSH window.
    *   Select **Download file**.
    *   Enter the full path to the file: `/home/YOUR_USERNAME/image_processing_project/outputs.zip`
    *   (You can find your username by typing `whoami` and the current path by typing `pwd`).

---

## Step 8: Clean Up

**Important:** Don't forget to **STOP** or **DELETE** your VM instance when you are finished to avoid being charged!
