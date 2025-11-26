from abc import ABC, abstractmethod
from dataclasses import dataclass
import logging


MONITOR_GOOD = "good"
MONITOR_BAD = "bad"


@dataclass
class MonitorStatus:
    name: str
    status: str


class BaseMonitor(ABC):
    @property
    @abstractmethod
    def monitor_name(self) -> str:
        pass

    async def get_monitor_result(self):
        logging.getLogger(__name__).info(f"Getting status for {self.monitor_name}")
        status = await self.get_status()
        return MonitorStatus(self.monitor_name, status)

    @abstractmethod
    async def get_status(self) -> str:
        pass
