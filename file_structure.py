 
import os

# Define the project directory and subdirectories
root_dir = "real-time-data-visualization"
data_dir = os.path.join(root_dir, "data")
processing_dir = os.path.join(root_dir, "processing")
visualization_dir = os.path.join(root_dir, "visualization")

# Define the files to create in each directory
data_files = ["tweets.csv", "sensors.csv"]
processing_files = ["kinesis.py", "lambda.py", "s3.py"]
visualization_files = ["dashboard.py", "filters.py", "plots.py"]

# Check if the root directory exists, if not create it
if not os.path.exists(root_dir):
    os.mkdir(root_dir)

# Create the data directory and files
if not os.path.exists(data_dir):
    os.mkdir(data_dir)
for file in data_files:
    open(os.path.join(data_dir, file), 'a').close()

# Create the processing directory and files
if not os.path.exists(processing_dir):
    os.mkdir(processing_dir)
for file in processing_files:
    open(os.path.join(processing_dir, file), 'a').close()

# Create the visualization directory and files
if not os.path.exists(visualization_dir):
    os.mkdir(visualization_dir)
for file in visualization_files:
    open(os.path.join(visualization_dir, file), 'a').close()

# Print success message
print("File structure and empty files created successfully!")
