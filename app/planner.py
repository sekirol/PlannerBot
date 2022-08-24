#!/usr/bin/env python3

from datetime import datetime

class Planner:
    def __init__(self):
        self.tasks_list = []    

    def create_task(self, task_title: str, start_time: str = None, 
                    duration: str = None, group: str = None):
        
        if not start_time:
            start_time = self._get_task_start_time()

        self.tasks_list.append(Task(task_title, start_time, duration, group))

    def _get_task_start_time(self):
        pass
    
    @staticmethod
    def get_user_groups() -> dict:
        return [{"name":"Простая", "id": 1},
                {"name":"Срочная", "id": 2},
                {"name":"На будущее", "id": 3}]