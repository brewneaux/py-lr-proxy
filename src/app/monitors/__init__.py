import asyncio
from .homeassistant import HomeAssistant
from .julep_feeder import JulepFeeder
from .blinds import BlindBatteries
from .internet import Internet
from .scrypted import Scrypted
from .doorbell import Doorbell


__all__ = ["HomeAssistant", "JulepFeeder", "BlindBatteries", "Internet", "Scrypted", "Doorbell"]

MONITORS = [HomeAssistant, JulepFeeder, BlindBatteries, Internet, Scrypted, Doorbell]


async def get_all_monitors():
    monitor_results = await asyncio.gather(*[m().get_monitor_result() for m in MONITORS])
    print(monitor_results)
    return monitor_results
