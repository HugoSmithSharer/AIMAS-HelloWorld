from metagpt.actions import Action

class ProductManagerAction(Action):
    name: str = "ProductManagerAction"

    async def run(self, msg: str) -> str:
        response = await self._aask(msg)
        return f"Product Manager says: {response}"