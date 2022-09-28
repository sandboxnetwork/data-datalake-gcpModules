from .base_handler import BaseHandler
from google.cloud import storage
from google.oauth2 import service_account


class StorageHandler(BaseHandler):
    def __init__(self, **kwargs):
        """Class for reading files from Cloud Storage

        kwargs:
            storage (Optional, string): name of cloud storage
            path (Optional, string): download path, default "../downloads/"

        Raises:
            Exception: Check for 'project_name/settings.json'
        """
        super().__init__(**kwargs)
        self._f_path = kwargs.get("path", self._f_path)
        self._b_name = kwargs.get("storage", "")

    # Get Cloud Storage object
    def __get_cloud_storage_client(self):
        cred = service_account.Credentials.from_service_account_info(
            {
                "type": "service_account",
                "project_id": self._g_proj,
                "private_key_id": self._g_key_id,
                "private_key": self._g_key,
                "client_email": self._g_mail,
                "client_id": self._g_cl_id,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_x509_cert_url": self._g_cl_url,
            },
            scopes=["https://www.googleapis.com/auth/devstorage.read_only"],
        )
        return storage.Client(credentials=cred, project=cred.project_id)

    # Get Cloud Storage object
    def __get_cloud_storage_blob(self, name):
        client = self.__get_cloud_storage_client()
        bucket = client.bucket(self._b_name)
        return bucket.blob(name)
    
    #
    def exists(self, name):
        """ check whether file exists in cloud storage

        Args:
            name (string): name of the file to check existence

        Returns:
            bool : return true if exists, else false
        """
        blob = self.__get_cloud_storage_blob(name)
        return blob.exists()

    #
    def list(self, prefix=None, nested=True):
        """ get list of files from cloud storage

        Args:
            prefix (string, optional): search file name by its prefix. Defaults to None.
            nested (bool, optional): if True, search files including its subdirectories. Defaults to True.

        Returns:
            list : file name list
        """
        client = self.__get_cloud_storage_client()
        delimiter = None if nested else "/"
        blob_iter = client.list_blobs(self._b_name, prefix=prefix, delimiter=delimiter)
        return [blob.name for blob in blob_iter]

    def download(self, nlist):
        """download single or multiple files from cloud storage

        Args:
            nlist (list or string): file name or list of file names to be downloaded

        Returns:
            tuple: file names downloaded (successful, failed)
        """
        if type(nlist) is not list: nlist = [nlist]
        downloaded = []
        failed = []

        for name in nlist:
            try:
                fpath = self.__get_file_path(name)
                blob = self.__get_cloud_storage_blob(name)
                blob.download_to_filename(fpath)
            except:
                failed.append(name)
            else:
                downloaded.append(name)
        return (downloaded, failed)