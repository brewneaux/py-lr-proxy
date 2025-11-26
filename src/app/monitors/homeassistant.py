import httpx
from app.config import settings
from app.monitors.base import MONITOR_GOOD, MONITOR_BAD, BaseMonitor
from logging import getLogger


class HomeAssistant(BaseMonitor):
    def __init__(self):
        s = settings()
        self._url = s.ha_url
        self._token = s.ha_token

    @property
    def monitor_name(self):
        return "HomeAssistant"

    async def get_status(self):
        headers = {"Authorization": f"Bearer {self._token}"}
        try:
            async with httpx.AsyncClient(headers=headers) as client:
                r = await client.get(self._url, headers=headers)
            if r.status_code == httpx.codes.OK and r.json().get("message") == "API running.":
                return MONITOR_GOOD
            getLogger(__name__).warning(f"Returning MONITOR_BAD from {self._url}: {r.text}")
            return MONITOR_BAD
        except httpx.HTTPError as e:
            getLogger(__name__).warning(f"Unable to connect to HomeAssistant at {self._url}", exc_info=e)
            return MONITOR_BAD
