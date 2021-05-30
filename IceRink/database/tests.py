from django.test import TestCase
from .utils import DataBaseAPI, ReminderAPI
from datetime import date

class TestDataBaseAPI(TestCase):
    def setUp(self) -> None:
        self.db_api = DataBaseAPI()
        self.reminder = ReminderAPI()
        self.data_for_make_record = {
            'visitor_name': 'some_name',
            'visitor_email': 'some_email',
            'date': '2021-05-26'
        }

    def test_API(self):
        self.assertEqual(self.db_api.make_record(self.data_for_make_record), None)
        record = self.db_api.get_visitor_record(self.data_for_make_record['visitor_name'])
        print(*record)
        self.assertEqual(self.db_api.queue_is_full(record[0].date), True)
        self.assertEqual(*self.reminder.get_reminder(self.data_for_make_record['visitor_name']), *record)


