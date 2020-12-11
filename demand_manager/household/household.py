from demand_manager.household.task import *
from demand_manager.time.time import *


class Household:

    def __init__(self):
        self.data = dict()
        self.time = dict()

    def set_scheduling_horizon(self, scheduling_horizon=1440, scheduling_interval_duration=10,
                               pricing_period_duration=30):
        time = Time()
        time.set_data(scheduling_horizon=scheduling_horizon,
                      scheduling_interval_duration=scheduling_interval_duration,
                      pricing_period_duration=pricing_period_duration)
        self.time = time.data

    def add_new_task(self, task_id, demand, preferred_start, latest_finish, demand_profile=(), earliest_start=0,
                     duration=1, care_factor=0, successor=(), precedent=()):
        task = Task()
        task.set_data(task_id=task_id, demand=demand, preferred_start=preferred_start, latest_finish=latest_finish,
                      demand_profile=demand_profile, earliest_start=earliest_start, duration=duration,
                      care_factor=care_factor, successor=successor, precedent=precedent)
        self.data[task_id] = task.to_dict()

    def schedule_tasks(self, prices, solver=s_solver, language=s_language, pre_processing=True,
                       minimise_usage=True, minimise_discomfort=True):
        if language == s_language:
            schedule_minizinc(self.time, prices, pre_processing, minimise_usage, minimise_discomfort)
        else:
            # default to use minizinc and a cp solver
            schedule_minizinc(self.time, prices, pre_processing, minimise_usage, minimise_discomfort)


def __convert_prices(prices, time_dict):
    len_prices = len(prices)
    if len_prices == time_dict[k_num_pricing_period]:
        num_scheduling_per_pricing = time_dict[k_num_scheduling_per_pricing]
        prices_converted = [x for x in prices for _ in range(num_scheduling_per_pricing)]
    elif len_prices == time_dict[k_num_scheduling_interval]:
        prices_converted = prices
    else:
        sys.exit(f"The length of the prices doesn't match the number of pricing periods/scheduling intervals. ")

    return prices_converted


def schedule_minizinc(time_dict, prices, pre_processing, minimise_usage, minimise_discomfort):
    num_scheduling = time_dict[k_num_scheduling_interval]
    prices_converted = __convert_prices(prices, time_dict)

    # todo: write the minizinc model --- need time to think
    return 0
