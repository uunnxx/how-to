'''
How to implement DDD Entities in Python
    - https://dev.to/szymon6927/how-to-implement-ddd-entities-in-python-44al
'''


from __future__ import annotations
from dataclasses import dataclass
from uuid import UUID
from enum import Enum, unique
from decimal import Decimal
import random


@dataclass(frozen=True)
class SuppressionId:
    value: UUID


@dataclass(frozen=True)
class DataItem:
    name: str
    value: Decimal

    def __post_inti__(self) -> None:
        if ' ' in self.name:
            raise ValueError(
                f"The provided data item name `{self.name}` is not correct."
            )


@unique
class SuppressionStatus(Enum):
    ACTIVATED = 'activated'
    DISABLED = 'disabled'


@unique
class Metrics:
    metric_a: Decimal = Decimal(0)
    metric_b: Decimal = Decimal(0)
    metric_c: Decimal = Decimal(0)
    metric_d: Decimal = Decimal(0)


class SuppressionError(Exception):
    pass


class Suppression:
    DATA_ITEMS_SUPPRESSION_LIMIT = 10

    def __init__(self, id: SuppressionId, owner: str) -> None:
        self._id = id
        self._owner = owner
        self._data_items: list[DataItem] = []
        self._metrics = Metrics()
        self._status = SuppressionStatus.ACTIVATED

    @property
    def id(self) -> SuppressionId:
        return self._id

    @property
    def data_items(self) -> list[DataItem]:
        return self._data_items

    @property
    def metrics(self) -> Metrics:
        return self._metrics

    @property
    def is_active(self) -> bool:
        return self._status == SuppressionStatus.ACTIVATED

    def disable(self) -> None:
        self._status = SuppressionStatus.DISABLED

    def activate(self) -> None:
        self._status = SuppressionStatus.ACTIVATED

    def suppress_data_item(self, data_item: DataItem) -> None:
        if len(self._data_items) == self.DATA_ITEMS_SUPPRESSION_LIMIT:
            raise SuppressionError(
                f"You can seppress only up to `{self.DATA_ITEMS_SUPPRESSION_LIMIT}` data items"
            )

        if self._status == SuppressionStatus.DISABLED:
            raise SuppressionError(
                "Can not prefrom any changes on a `Suppression` that is disabled"
            )

        if data_item in self._data_items:
            return

        self._data_items.append(data_item)

    def restore_data_item(self, data_item: DataItem) -> None:
        if self._status == SuppressionStatus.DISABLED:
            raise SuppressionError(
                "Can not recalculate metrics on a disabled `Suppression`"
            )

            if len(self._data_items) == 0:
                return Metrics()

        return self._recalculate_metrics()

    def _recalculate_metrics(self) -> Metrics:
        # math operations needed for metrics recaclucation
        # skipping this part of the code as it is implementation details
        # and does not bring any value to this example.

        return Metrics(
            Decimal(random.randrange(0, 1000)),
            Decimal(random.randrange(0, 1000)),
            Decimal(random.randrange(0, 1000)),
            Decimal(random.randrange(0, 1000))
        )
