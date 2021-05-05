from enum import unique
from peewee import *
import os

db = SqliteDatabase('haberler.db')

class BaseModel(Model):
    class Meta:
        database=db

class Haberler(BaseModel):
    haber=CharField(unique=True)


if __name__ == '__main__':
    db.connect()
    db.create_tables([Haberler], safe=True)