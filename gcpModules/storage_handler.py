from .base_handler import BaseHandler
from google.cloud import storage
from google.oauth2 import service_account
import os, csv, json


class StorageHandler(BaseHandler):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._bucket = kwargs.get("bucket")
        self._file_path = kwargs.get("file_path")

    # Get Cloud Storage object
    def __get_cloud_storage_client(self):
        cred = service_account.Credentials.from_service_account_info(
            self._credentials,
            scopes=["https://www.googleapis.com/auth/devstorage.read_only"],
        )
        return storage.Client(credentials=cred, project=cred.project_id)

    def set_bucket(self, bucket):
        self._bucket = bucket
    
    def set_file_path(self, file_path):
        self._file_path = file_path

    # Get Cloud Storage object
    def __get_cloud_storage_blob(self, name):
        client = self.__get_cloud_storage_client()
        bucket = client.bucket(self._bucket)
        return bucket.blob(name)
    
    #
    def exists(self, name, bucket=None):
        if bucket:
            self.set_bucket(bucket)
        blob = self.__get_cloud_storage_blob(name)
        return blob.exists()

    #
    def list(self, bucket=None, prefix=None, nested=True):
        if bucket:
            self.set_bucket(bucket)
        client = self.__get_cloud_storage_client()
        delimiter = None if nested else "/"
        return list(client.list_blobs(self._bucket, prefix=prefix, delimiter=delimiter))

    def read(self, blob_list, file_path=None):
        fpath_list = self.download(blob_list, file_path)
        if len(fpath_list) > 1:
            print(f"Must input one file to read, file count: f{len(fpath_list)}")
        
        fname = fpath_list[0]
        if fname.endswith(".json"):
            with open(fname, "r", encoding="UTF-8") as dest_file:
                return json.load(dest_file)
        elif fname.endswith(".csv"):
            _result = []
            _reader = csv.reader(dest_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            for _r in _reader:
                _result.append(_r)
            return _result

    def download(self, blob_list, file_path=None):
        fpath_list = []
        for blob in blob_list:
            if(not blob.name.endswith("/")):
                fname = blob.name.split("/")[-1]
                fpath = os.path.join(file_path, fname) if file_path else os.path.join(self._file_path, fname)
                blob.download_to_filename(fpath)
                fpath_list.append(fpath)
        return fpath_list