import httpx
from logging import getLogger
from app.config import settings
from app.monitors.base import MONITOR_GOOD, MONITOR_BAD, BaseMonitor


class Scrypted(BaseMonitor):
    def __init__(self):
        s = settings()
        self._url = s.scrypted_url

    @property
    def monitor_name(self):
        return "Scrypted"

    async def get_status(self):
        try:
            async with httpx.AsyncClient(verify=False) as client:
                r = await client.get(self._url)
            if r.status_code == httpx.codes.OK:
                return MONITOR_GOOD
            return MONITOR_BAD
        except httpx.HTTPError as e:
            getLogger(__name__).warning(f"Received bad response from {url}", exc_info=e)
            return MONITOR_BAD
