import peewee

db = peewee.SqliteDatabase('database.db')

class Number(peewee.Model):
    sequence = peewee.IntegerField()
    label = peewee.CharField()

    class Meta:
        database = db
        order_by = ('sequence',)
