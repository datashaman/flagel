import os
import peewee


db = peewee.SqliteDatabase(os.getenv('DB'))

class Number(peewee.Model):
    sequence = peewee.IntegerField()
    label = peewee.CharField()

    class Meta:
        database = db
        order_by = ('sequence',)
