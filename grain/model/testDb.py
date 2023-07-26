from grain.libs.database import db


class Test(db.Model):
    __tablename__ = 'test'
    test_id = db.Column(db.String(50), primary_key=True)

    __table_args__ = {'extend_existing': True}

    def __init__(self, test_id):
        self.test_id = test_id

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}
