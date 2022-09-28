import os, json

from pathlib import Path

class BaseHandler:
    def __init__(self, **kwargs):
        _ORIG_PATH = str(Path(__file__).resolve().parent.parent)
        _JSON_PATH = os.path.join(_ORIG_PATH, "settings.json")

        self._f_path = os.path.join(_ORIG_PATH, "downloads")
        Path(self._f_path).mkdir(parents=True, exist_ok=True)

        if os.path.isfile(_JSON_PATH):
            with open(_JSON_PATH, "r", encoding="UTF-8") as envs:
                self._ev_datas = json.load(envs)
        else:
            raise Exception("Need Settings.json")

        self._g_proj = self._ev_datas.get("GCP_SK_PROJECT_ID", "")
        self._g_key_id = self._ev_datas.get("GCP_SK_PRIVATE_KEY_ID", "")
        self._g_key = self._ev_datas.get("GCP_SK_PRIVATE_KEY", "").replace("\\n", "\n")
        self._g_mail = self._ev_datas.get("GCP_SK_CLIENT_EMAIL", "")
        self._g_cl_id = self._ev_datas.get("GCP_SK_CLIENT_ID", "")
        self._g_cl_url = self._ev_datas.get("GCP_SK_CERT_URL", "")
    
    # Get file path string
    def __get_file_path(self, name):
        return os.path.join(self._f_path, name)
