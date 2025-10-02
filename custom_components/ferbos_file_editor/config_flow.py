from __future__ import annotations
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from .const import DOMAIN
import voluptuous as vol


class FerbosFileEditorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None) -> FlowResult:
        if user_input is not None:
            return self.async_create_entry(title="Ferbos File Editor", data={})

        return self.async_show_form(step_id="user", data_schema=vol.Schema({}))
