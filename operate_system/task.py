# -*- coding: utf-8 -*-
import threading
import uuid


class Task(object):
    def __init__(self, func, *args, **kwargs):
        self.callable = func
        self.id = uuid.uuid4()
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return f"Task id: {self.id}"


class AsyncTask(Task):
    def __init__(self, func, *args, **kwargs):
        self.result = None
        self.condition = threading.Condition()
        super(AsyncTask, self).__init__(func, *args, **kwargs)

    def set_result(self, result):
        self.condition.acquire()
        self.result = result
        self.condition.notify()
        self.condition.release()

    def get_result(self):
        self.condition.acquire()
        if not self.result:
            self.condition.wait()
        result = self.result
        self.condition.release()
        return result
