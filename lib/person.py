#!/usr/bin/env python3



class Person:
    APPROVED_JOBS = approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]
    
   

    def __init__(self, name="", job=""):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be a string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in self.APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
