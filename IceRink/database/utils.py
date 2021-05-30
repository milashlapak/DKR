from .models import VisitorRecord
from datetime import date


class DataBaseAPI:
    def __init__(self):
        self.records = VisitorRecord.objects.all()

    def make_record(self, data):
        new_record = VisitorRecord(**data)
        if self.queue_is_full(new_record.date):
            new_record.save()
        else:
            raise Exception

    def queue_is_full(self, date: date) ->bool:
        records = self.records.filter(date=date)
        if len(records) > 40:
            return False
        return True

    def get_visitor_record(self, username):
        records = self.records.filter(visitor_name=username)
        records = self.clean_record(records)
        return records

    def clean_record(self, records):
        today = date.today()
        for record in records:
            if record.date < today:
                records.remove(record)
        return records

class ReminderAPI:
    def __init__(self):
        self.records = VisitorRecord.objects.all()

    def get_reminder(self, username):
        record = self.records.filter(visitor_name=username)
        today_date = date.today()
        record = record.filter(date=today_date)
        return record
