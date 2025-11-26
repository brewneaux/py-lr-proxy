from app.config import settings
from app.monitors.homeassistant_entitiy_monitor_base import HomeAssistantEntityBaseMonitor


class JulepFeeder(HomeAssistantEntityBaseMonitor):
    """This uses HomeAssistant to expose the PetKit data - since an account can only be used one place at a time, this is much more convenient."""

    def __init__(self):
        s = settings()
        self._url = s.ha_entities_url
        self._token = s.ha_token

    @property
    def entities(self):
        return ["binary_sensor.freshelement_3_food_level"]

    @property
    def monitor_name(self):
        return "JulepFeeder"

    def check_entity(self, entity_dict):
        return entity_dict.get("state") == "off"
