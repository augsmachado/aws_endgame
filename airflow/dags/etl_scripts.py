import os
import glob
from airflow.hooks.S3_hook import S3Hook


def local_to_s3(bucket_name, filepath="./dags/data/*.csv"):
    s3 = S3Hook()

    for f in glob.glob(filepath):
        key = "bacen_data/" + f.split("/")[-1]
        s3.load_file(filename=f, bucket_name=bucket_name, replace=True, key=key)


def remove_local_file(filepath="./dags/data/*.csv"):
    files = glob.glob(filepath)
    for f in files:
        os.remove(f)
