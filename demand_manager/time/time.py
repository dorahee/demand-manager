import sys
import warnings
from demand_manager.time.parameters import *


class Time:

    def __init__(self):
        self.scheduling_horizon = 1440
        self.scheduling_interval_duration = 10
        self.pricing_period_duration = 30
        self.num_scheduling_interval = int(self.scheduling_horizon / self.scheduling_interval_duration)
        self.num_pricing_period = int(self.scheduling_horizon / self.pricing_period_duration)
        self.num_scheduling_per_pricing = self.num_scheduling_interval / self.num_pricing_period
        self.data = dict()

    def set_data(self, scheduling_horizon=1440, scheduling_interval_duration=10, pricing_period_duration=30):

        self.scheduling_horizon = scheduling_horizon
        self.scheduling_interval_duration = scheduling_interval_duration
        self.pricing_period_duration = pricing_period_duration

        self.num_scheduling_interval = self.scheduling_horizon / self.scheduling_interval_duration
        if self.num_scheduling_interval % 1 != 0:
            warnings.warn(f'The number of scheduling interval per day {self.num_scheduling_interval} '
                          f'has been rounded down to a whole number.')
            self.num_scheduling_interval = int(self.num_scheduling_interval)

        self.num_pricing_period = self.scheduling_horizon / self.pricing_period_duration
        if self.num_pricing_period % 1 != 0:
            warnings.warn(f'The number of scheduling interval per day {self.num_pricing_period} '
                          f'has been rounded down to a whole number.')
            self.num_pricing_period = int(self.num_pricing_period)

        self.num_scheduling_per_pricing = self.num_scheduling_interval / self.num_pricing_period
        if self.num_scheduling_per_pricing % 1 != 0:
            sys.exit(f"The number of scheduling intervals per pricing period {self.num_scheduling_per_pricing} "
                     f"is not whole. ")

    def to_dict(self):
        self.data = {
            k_scheduling_horizon: self.scheduling_horizon,
            k_scheduling_interval_duration: self.scheduling_interval_duration,
            k_pricing_period_duration: self.pricing_period_duration,
            k_num_scheduling_interval: self.num_scheduling_interval,
            k_num_pricing_period: self.num_pricing_period,
            k_num_scheduling_per_pricing: self.num_scheduling_per_pricing,
        }
        return self.data
