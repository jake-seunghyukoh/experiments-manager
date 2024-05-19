from dataclasses import dataclass, field

from .abstract import AbstractEntity


@dataclass
class Experiment(AbstractEntity):
    # Metadata
    run_name: str = field(default=None)
    experiment_name: str = field(default=None)

    # Status
    status: str = field(default="pending")
    status_message: str = field(default=None)
    script: str = field(default=None)

    NOT_ALLOWED_KEYS_UPDATE = [
        "id",
        "run_name",
        "experiment_name",
        "created_at",
        "created_at_timestamp",
        "updated_at",
        "updated_at_timestamp",
    ]

    @staticmethod
    def create(**kwargs):
        return AbstractEntity.create(Experiment, **kwargs)

    def validate(self):
        super().validate()

        assert self.run_name is not None
        assert self.experiment_name is not None

        assert self.status in ["pending", "running", "completed"]
        assert self.status_message is None or isinstance(self.status_message, str)
        assert self.script is None or isinstance(self.script, str)

    def update(self, data):
        for key in Experiment.NOT_ALLOWED_KEYS_UPDATE:
            assert key not in data, f"Key {key} is not allowed to be updated"

        self.__dict__.update(data)

        self.update_timestamp()

        self.validate()
