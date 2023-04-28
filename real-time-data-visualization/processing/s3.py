python
import boto3

BUCKET_NAME = "my-bucket-name"

# Create an S3 client
s3 = boto3.client('s3')

def process_s3_data():
    """
    This function downloads data from an S3 bucket and processes it.
    """
    # Download the data from the bucket
    s3.download_file(BUCKET_NAME, "data.csv", "data.csv")

    # Process the data here
    df = pd.read_csv("data.csv")
    # Some data processing steps...
    
    # Upload the processed data back to S3
    s3.upload_file("processed_data.csv", BUCKET_NAME, "processed_data.csv")
