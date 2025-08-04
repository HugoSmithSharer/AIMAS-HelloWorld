from typing import ClassVar
from metagpt.actions import Action
from metagpt.config2 import Config

llm_config = Config.from_home("config2.yaml")

class DeveloperAction(Action):
    name: str = "DeveloperAction"
    config: ClassVar[Config] = Config.from_home("config2.yaml")

    async def run(self, msg: str) -> str:
        response = await self._aask(msg)
        return f"Developer says: {response}"