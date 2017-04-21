from boto.s3.connection import S3Connection
from boto.s3.key import Key
import os

def init_s3():
    #REGION_HOST = 's3.us-east-2.amazonaws.com'
    REGION_HOST = os.environ["AWS_REGION"]
    BUCKET_NAME = os.environ["BUCKET_NAME"]
    conn = S3Connection(os.environ['AWS_ID'], os.environ['AWS_SECRET'], host=REGION_HOST)
    mybucket = conn.get_bucket(BUCKET_NAME)
    for file in os.listdir("data/files"):
            k = Key(mybucket)
            k.key = file
            k.set_contents_from_filename(os.path.join("data/files/", file))
    clear_all()

def clear_all():
    import shutil
    shutil.rmtree('data/files')
    os.makedirs('data/files')