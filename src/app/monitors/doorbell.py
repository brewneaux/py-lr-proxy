import httpx
from logging import getLogger
from app.config import settings
from app.monitors.base import MONITOR_GOOD, MONITOR_BAD, BaseMonitor


class Doorbell(BaseMonitor):
    def __init__(self):
        s = settings()
        self._url = s.doorbell_url
        self._username = s.doorbell_username
        self._password = s.doorbell_password

    @property
    def monitor_name(self):
        return "Doorbell"

    async def get_status(self):
        try:
            auth = httpx.DigestAuth(self._username, self._password)
            async with httpx.AsyncClient(verify=False, auth=auth) as client:
                r = await client.get(self._url)
            if r.status_code == httpx.codes.OK and r.json()["success"]:
                return MONITOR_GOOD

            getLogger(__name__).warning(f"Received bad response from {self._url}: {r.status_code} {r.text}")

            return MONITOR_BAD
        except httpx.HTTPError as e:
            getLogger(__name__).warning(f"Unable to contact doorbell at {self._url}", exc_info=e)
            return MONITOR_BAD
