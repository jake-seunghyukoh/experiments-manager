import hashlib
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class AbstractEntity(ABC):
    id: str = field(default=None)

    # Timestamps
    created_at: str = field(default=None)
    created_at_timestamp: float = field(default=None)
    updated_at: str = field(default=None)
    updated_at_timestamp: float = field(default=None)

    NOT_ALLOWED_KEYS_CREATE = [
        "id",
        "created_at",
        "created_at_timestamp",
        "updated_at",
        "updated_at_timestamp",
    ]
    NOT_ALLOWED_KEYS_UPDATE = [
        "id",
        "created_at",
        "created_at_timestamp",
        "updated_at",
        "updated_at_timestamp",
    ]

    @staticmethod
    @abstractmethod
    def create(cls, **kwargs):
        for key in cls.NOT_ALLOWED_KEYS_CREATE:
            assert key not in kwargs

        entity = cls(**kwargs)
        entity.set_timestamp()

        entity.id = cls.hash_data(kwargs)

        entity.validate()
        return entity

    @staticmethod
    def hash_data(data):
        return hashlib.sha256(str(data).encode()).hexdigest()

    def set_timestamp(self):
        self.created_at = time.ctime()
        self.created_at_timestamp = time.time()
        self.updated_at = None
        self.updated_at_timestamp = None

    def update_timestamp(self):
        self.updated_at = time.ctime()
        self.updated_at_timestamp = time.time()

    def to_dict(self):
        return self.__dict__

    def validate(self):
        assert self.id is not None
        assert self.created_at is not None
        assert self.created_at_timestamp is not None

        if self.updated_at is not None:
            assert self.updated_at_timestamp is not None

            # updated_at_timestamp should be greater than created_at_timestamp
            assert self.updated_at_timestamp > self.created_at_timestamp
