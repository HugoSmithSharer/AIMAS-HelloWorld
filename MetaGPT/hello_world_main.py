import asyncio
from metagpt.roles import Role
from metagpt.schema import Message
from developer_role import DeveloperRole
from product_manager_role import ProductManagerRole

async def ProductManagerAgent(input: str):
    productManager = ProductManagerRole(goal="Decompose a feature to a number of tasks for Developer to implement")
    msg = Message(content=input, role="user")
    response = await productManager.run(msg)
    return response.content

async def DeveloperAgent(input: str):
    developer = DeveloperRole(goal="Implement the tasks passed from Product Manager")
    msg = Message(content=input, role="user")
    response = await developer.run(msg)
    return response.content

async def main():
    productManagerResponse = await ProductManagerAgent(input="I need your help to write hello world in python")
    print("Product Manager says: ", productManagerResponse)
    developerResponse = await DeveloperAgent(input=productManagerResponse)
    print("Developer says: ", developerResponse)

if __name__ == "__main__":
    asyncio.run(main())