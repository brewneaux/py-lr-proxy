import logging
from app.config import settings
from app.monitors.homeassistant_entitiy_monitor_base import HomeAssistantEntityBaseMonitor


class BlindBatteries(HomeAssistantEntityBaseMonitor):
    def __init__(self):
        s = settings()
        self._url = s.ha_entities_url
        self._token = s.ha_token

    @property
    def monitor_name(self):
        return "BlindsBatteries"

    @property
    def entities(self):
        return [
            "sensor.blinds_left_battery_level",
            "sensor.blinds_middle_battery_level",
            "sensor.blinds_right_battery_level",
        ]

    def check_entity(self, entity_dict: dict) -> bool:
        is_good = float(entity_dict.get("state", "0.0")) > 20
        logging.getLogger(__name__).info(f"Checking entity {entity_dict}")
        if not is_good:
            logging.getLogger(__name__).warning(f"Returning monitor_bad for {self.monitor_name}: {entity_dict}")
        return is_good
