import httpx
from logging import getLogger
from app.monitors.base import MONITOR_GOOD, MONITOR_BAD, BaseMonitor


class Internet(BaseMonitor):
    @property
    def monitor_name(self):
        return "Internet"

    async def get_status(self):
        url = "http://www.msftncsi.com/ncsi.txt"
        try:
            async with httpx.AsyncClient() as client:
                r = await client.get(url)
            if r.status_code == httpx.codes.OK and r.text == "Microsoft NCSI":
                return MONITOR_GOOD
            return MONITOR_BAD
        except httpx.HTTPError as e:
            getLogger(__name__).warning(f"Received bad response from {url}", exc_info=e)
            return MONITOR_BAD
