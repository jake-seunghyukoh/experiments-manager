import pprint

from colored import Fore, Style

from use_cases import create_experiment, update_experiment


def print_experiments(experiments, title=""):
    print(title)
    if not isinstance(experiments, list):
        experiments = [experiments]

    for experiment in experiments:
        pprint.pprint(experiment.__dict__)

    print()


if __name__ == "__main__":
    experiment = create_experiment(
        run_name="test_run", experiment_name="text_experiment"
    )
    print_experiments(experiment, title=f"{Fore.red}Initial Experiment{Style.reset}")

    update_experiment(experiment, dict(status="running"))
    print_experiments(experiment, title=f"{Fore.yellow}Updated Experiment{Style.reset}")
