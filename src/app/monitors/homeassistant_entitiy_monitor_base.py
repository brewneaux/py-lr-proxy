from abc import ABC, abstractmethod
from typing import List
import httpx
from app.config import settings
from app.monitors.base import MONITOR_GOOD, MONITOR_BAD, BaseMonitor
from logging import getLogger


class HomeAssistantEntityBaseMonitor(BaseMonitor, ABC):
    def __init__(self):
        s = settings()
        self._url = s.ha_url
        self._token = s.ha_token

    @property
    @abstractmethod
    def entities(self) -> List[str]:
        pass

    @abstractmethod
    def check_entity(self, entity_dict: dict) -> bool:
        pass

    async def _get_single_entity_status(self, client, entity):
        url = self._url + f"{entity}"
        try:
            resp = await client.get(url)
            if resp.status_code == httpx.codes.OK and self.check_entity(resp.json()):
                return MONITOR_GOOD
            return MONITOR_BAD
        except httpx.HTTPError as e:
            getLogger(__name__).warning(f"Unable to get HomeAssistant Entity Status for {entity} at {url}", exc_info=e)
            return MONITOR_BAD

    async def get_status(self):
        headers = {"Authorization": f"Bearer {self._token}"}
        entity_statuses = []
        getLogger(__name__).info(f"Getting statuses for {self.monitor_name}")
        for e in self.entities:
            async with httpx.AsyncClient(headers=headers) as client:
                e_status = await self._get_single_entity_status(client, e)
                entity_statuses.append(e_status)
        return MONITOR_GOOD if all(x == MONITOR_GOOD for x in entity_statuses) else MONITOR_BAD
