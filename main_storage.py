import platform
import os

import pandas as pd

import google.cloud.storage as gcs

print('Hello ... running Python:', platform.python_version())

def upload_file(file_name, bucket):
    blob = bucket.blob(os.path.basename(source_file_name))
    # Upload the local file to Cloud Storage.
    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        bucket))


print('Create a storage client')
storage_client = gcs.Client()
print('Storage client created successfully')
bucket_name = 'itllctl-01'
bucket = storage_client.get_bucket(bucket_name)

# upload file
source_file_name = '/tmp2/NRSRO_Exhibit-1.pdf' #'20141222_133915.jpg'
#upload_file(source_file_name, bucket)

# list files
print('files in bucket')
blobs = bucket.list_blobs()
total_size = 0

for blob in blobs:
    print("Filename: %s, Size: %5.2f MB" % (blob.name,blob.size/1024/1024))
    total_size = total_size + blob.size

total_size_MB = total_size/(1000**2)
number_of_files = blobs.num_results
print('\nBucket <%s> holds %d files with total size of %.2f MB' % (bucket_name, number_of_files, total_size_MB))
