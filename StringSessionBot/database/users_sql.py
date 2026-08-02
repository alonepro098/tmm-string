from sqlalchemy import Column, BigInteger
from StringSessionBot.database import BASE, SESSION


class Users(BASE):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}
    user_id = Column(BigInteger, primary_key=True)

    def __init__(self, user_id):
        self.user_id = user_id


if BASE and SESSION:
    try:
        Users.__table__.create(checkfirst=True)
    except Exception:
        pass


async def num_users():
    if not SESSION:
        return 0
    try:
        return SESSION.query(Users).count()
    except Exception:
        return 0
    finally:
        SESSION.close()
