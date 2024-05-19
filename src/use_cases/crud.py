from entities import Experiment


def create_experiment(**kwargs):
    experiment = Experiment.create(**kwargs)
    return experiment


def update_experiment(experiment, new_data):
    experiment.update(new_data)
