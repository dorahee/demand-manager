from demand_manager.household.parameters import *


class Task:

    def __init__(self):
        self.task_id = 0
        self.demand = 0
        self.demand_profile = ()
        self.duration = 1
        self.preferred_start = 0
        self.earliest_start = 0
        self.latest_finish = 0
        self.care_factor = 0
        self.successor = ()
        self.precedent = ()
        self.data = dict()

    def set_data(self, task_id, demand, preferred_start, latest_finish,
                 demand_profile=(), earliest_start=0, duration=1, care_factor=0, successor=(), precedent=()):
        self.task_id = task_id
        self.demand = demand
        self.preferred_start = preferred_start
        self.latest_finish = latest_finish
        self.demand_profile = demand_profile
        self.earliest_start = earliest_start
        self.duration = duration
        self.care_factor = care_factor
        self.successor = successor
        self.precedent = precedent

    def to_dict(self):
        self.data = {
            k_demand: self.demand,
            k_demand_profile: self.demand_profile,
            k_duration: self.duration,
            k_preferred_start: self.preferred_start,
            k_earliest_start: self.earliest_start,
            k_latest_finish: self.latest_finish,
            k_care_factor: self.care_factor,
            k_successor: self.successor,
            k_precedent: self.precedent,
        }
        return self.data
