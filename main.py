import platform
import os

import pandas as pd

import google.cloud.storage as gcs

print('Hello ... running Python:', platform.python_version())

print('Create a storage client')

storage_client = gcs.Client()

print('Storage client created successfully')

bucket_name = 'itllctl-01'
bucket = storage_client.get_bucket(bucket_name)

source_file_name = '/tmp2/20141222_133915.jpg'
blob = bucket.blob(os.path.basename(source_file_name))

# Upload the local file to Cloud Storage.
blob.upload_from_filename(source_file_name)

print('File {} uploaded to {}.'.format(
        source_file_name,
        bucket))