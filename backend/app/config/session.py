from sqlalchemy.orm import Session

class DatabaseSessionContext(object):
    def __init__(self, db: Session):
        self.db = db

class AppService(DatabaseSessionContext):
    pass