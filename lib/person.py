#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, job=""):
        self._job = ""
        self.job = job

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in self.APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs:", self.APPROVED_JOBS)
        
