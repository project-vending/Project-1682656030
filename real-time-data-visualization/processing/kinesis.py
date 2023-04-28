
import boto3

def main():
    # Set up kinesis client
    kinesis = boto3.client('kinesis')

    # Define Kinesis stream name
    stream_name = 'my_stream'

    # Create Kinesis stream
    try:
        response = kinesis.create_stream(
            StreamName=stream_name,
            ShardCount=1
        )
        print("Kinesis stream created successfully!")
    except Exception as e:
        if "ResourceInUseException" in str(e):
            print("Kinesis stream already exists.")
        else:
            print("Error creating Kinesis stream:", str(e))
            return

if __name__ == '__main__':
    main()
