import os
import peewee

from config import config, APP_ROOT


db = peewee.SqliteDatabase(os.path.join(APP_ROOT, config['database']))

class Number(peewee.Model):
    sequence = peewee.IntegerField()
    label = peewee.CharField()

    class Meta:
        database = db
        order_by = ('sequence',)

if not Number.table_exists():
    Number.create_table()

    numbers = (
        ('One', 1),
        ('Two', 2),
        ('Three', 3),
        ('Four', 4),
        ('Five', 5),
        ('Six', 6),
        ('Seven', 7),
        ('Eight', 8),
        ('Nine', 9),
        ('Ten', 10),
        ('Eleven', 11),
        ('Twelve', 12),
    )

    for label, sequence in numbers:
        Number.create(sequence=sequence, label=label)
