import os, json

from pathlib import Path

class BaseHandler:
    def __init__(self, **kwargs):
        self._credentials = kwargs.get("credentials", {})
