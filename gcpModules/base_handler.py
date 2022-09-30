import os, json

from pathlib import Path

class BaseHandler:
    def __init__(self, **kwargs):
        if "credentials" in kwargs:
            self._credentials = kwargs.get("credentials", {})
        elif "credential_path" in kwargs:
            cr_path = kwargs.get("credential_path", "")
            if os.path.isfile(cr_path):
                with open(cr_path, "r", encoding='UTF-8') as envs:
                    self._credentials = json.load(envs)
        else:
            raise Exception("Must enter either credentials or credential_path")
