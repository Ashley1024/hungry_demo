from flask_jsondash import db
from sqlalchemy import Column, Integer, String

"""
这是一个模型的例子（将代码放如models.py或类似文件中）
"""


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)
