#!/usr/bin/env python3

class Task:
    default_duration = 25
    default_group = "usual"

    def __init__(self, title: str, start_time: str, duration: str, group: str):
        self.title = title
        self.duration = duration if duration else Task.default_duration
        self.start_time = start_time
        self.group = group if group else Task.default_group

class Planner:
    def __init__(self):
        self.tasks_list = []    

    def create_task(self, task_title: str, start_time: str = None, 
                    duration: str = None, group: str = None):
        
        if not start_time:
            start_time = self._get_task_start_time()

        self.tasks_list.append(Task(task_title, start_time, duration))

    def _get_task_start_time(self):
        pass