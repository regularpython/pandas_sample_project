import pandas as pd
import boto3
import io
# Extract
s3 = boto3.client('s3')
# df = pd.read_csv(r"D:\Students\Class Explanation\45 Days Class\7-9 Pandas\data\car-rentals.csv")
# Define your bucket name and file path (key)
bucket_name = "jun-08-2026-batch"
file_key = "car-rentals-transformed.csv"
response = s3.get_object(Bucket=bucket_name, Key=file_key)
file_content = response['Body'].read().decode('utf-8')
# Convert the string content into a Pandas DataFrame
df = pd.read_csv(io.StringIO(file_content))



# # Transform
df['website'] = "RegularPython"

print("Hi")

# Load
# Destination bucket and file name
target_bucket = "jun-08-2026-batch"
target_key = "silver-transformed-derived-zone/cleaned_car_rentals_bookings_20260625.csv"

csv_buffer = io.StringIO()
df.to_csv(csv_buffer, index=False)  # index=False avoids saving row numbers
# 2. Upload the string data directly to S3
s3.put_object(
    Bucket=target_bucket,
    Key=target_key,
    Body=csv_buffer.getvalue()
)
print(f"Successfully uploaded data to s3://{target_bucket}/{target_key}")
# df.to_csv(r"D:\Students\Class Explanation\45 Days Class\7-9 Pandas\data\car-rentals-transformed.csv", index=False)
# print(df)