import os, json
from pathlib import Path
from .base_handler import BaseHandler
from google.oauth2 import service_account
from google.cloud import bigquery


class BigQueryHandler(BaseHandler):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Get Cloud Bigquery Client object
    def __get_cloud_bigquery_client(self):
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
                "client_x509_cert_url": self._g_cl_url
            },
            scopes=["https://www.googleapis.com/auth/bigquery"]
        )
        return bigquery.Client(
            credentials=cred,
            project=cred.project_id
        )

    def query(self, q, limit=50):
        cost = self.estimate(q)
        if cost > limit:
            return f"exceed limit({self.limit}), cost: {cost}"

        client = self.__get_cloud_bigquery_client()
        query_job = client.query(q)
        query_rst = [r for r in query_job.result()]
        return query_rst

    def estimate(self, q):
        job_config = bigquery.QueryJobConfig(dry_run=True)
        query_job = self.__get_cloud_bigquery_client().query((q), job_config=job_config)
        return query_job.total_bytes_processed / 1000 / 1000 / 1000
    
