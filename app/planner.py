#!/usr/bin/env python3

from datetime import datetime

class Task:
    default_duration = 25
    default_group = "usual"

    def __init__(self, title: str, start_time: str, duration: str, group: str):
        self._set_creation_time()

        self.title = title
        self.duration = duration if duration else Task.default_duration
        self.start_time = start_time
        self.group = group if group else Task.default_group

    def __str__(self) -> str:
        return f"Title: {self.title}\n" \
               f"Created: {self.creation_time}\n" \
               f"Duration: {self.duration}\n" \
               f"Start time: {self.start_time}\n" \
               f"Group: {self.group}\n"
    
    def _set_creation_time(self):
        self.creation_time = datetime.now().isoformat(sep=' ', timespec='seconds')
        
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