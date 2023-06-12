import sys


class Config:
    def __init__(self):
        sys.path.append(sys.path[0].replace('/contacts', '/'))
        import config as ac
        self.id = ac.api_id
        self.hash = ac.api_hash
