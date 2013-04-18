import os
import peewee

from apps import config


CONFIG = config.load_config('flagel')
APP_ROOT = config.app_root('flagel')

db = peewee.SqliteDatabase(os.path.join(APP_ROOT, CONFIG['database']))

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
