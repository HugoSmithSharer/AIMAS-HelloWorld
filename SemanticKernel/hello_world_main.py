import os
import dotenv
import asyncio
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion
from semantic_kernel.agents import ChatCompletionAgent, SequentialOrchestration
from semantic_kernel.agents.runtime import InProcessRuntime
import typing
from semantic_kernel.agents.orchestration.orchestration_base import OrchestrationBase
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents.utils.author_role import AuthorRole

async def main():
    dotenv.load_dotenv("SemanticKernel/.env")
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
    azure_deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
    azure_api_version = os.getenv("AZURE_OPENAI_API_VERSION")

    if not all([azure_endpoint, azure_api_key, azure_deployment]):
        print("Please set OPENAI_API_BASE, OPENAI_API_KEY, and OPENAI_API_MODEL environment variables in your .env file.")
        return

    kernel = sk.Kernel()
    kernel.add_service(
        AzureChatCompletion(
            deployment_name=azure_deployment,
            endpoint=azure_endpoint,
            api_key=azure_api_key,
            api_version=azure_api_version
        )
    )

    pm_agent = ChatCompletionAgent(
        kernel=kernel,
        name="pm_agent",
        instructions="""
            You are an experienced product manager with 8+ years of experience managing software products in high-growth startups. You excel at stakeholder collaboration, translating user needs into roadmap priorities, and balancing speed with quality. You believe in customer-centric product design and thrive in cross-functional environments. You will design and oversee product features, ensure user needs are met, and deliver a cohesive user experience that balances business viability and technical feasibility. Remember that you are a product manager and do not write code. You only decompose the feature as much as you can and pass to developers for implementation.
            Return tasks in JSON like: [{"task_id":1,"description":"..."},...].
            """
    )

    dev_agent = ChatCompletionAgent(
        kernel=kernel,
        name="dev_agent",
        instructions="""
        You are a senior software engineer named DevX with the goal of producing high quality software code. You were trained on thousands of GitHub repositories and have years of experience shipping production-grade code. You work best with clear specs but can reverse-engineer unclear requests when needed. You value clean, maintainable code and always leave things better than you found them, returning JSON: [{"task_id":1,"code":"..."}]. Avoid including any requirements in the output. Code only.
        """
    )

    # def patched_default_input_transform(self, task):
    #     t = getattr(self, "t_in", None)
    #     if t is None:
    #         return task

    #     # Determine acceptable base types
    #     base = typing.get_origin(t) or t
    #     args = getattr(t, "__args__", None)
    #     if args:
    #         # t is Union[...] or generic alias
    #         if typing.get_origin(t) is typing.Union:
    #             base = tuple(arg for arg in args if isinstance(arg, type))
    #         else:
    #             base = typing.get_origin(t) or t

    #     # Safe isinstance check
    #     if isinstance(task, base):
    #         return task
    #     return task

    # OrchestrationBase._default_input_transform = patched_default_input_transform
    
    orchestration = SequentialOrchestration(
        members=[pm_agent, dev_agent],
        agent_response_callback=lambda msg: print(f"> {msg.name} responded:\n{msg.content}\n")
    )

    runtime = InProcessRuntime()
    runtime.start()

    user_msg = ChatMessageContent(
        role=AuthorRole.USER,
        content="I need your help to write hello world in python."
    )

    result = await orchestration.invoke(
        task=user_msg,
        runtime=runtime)
    final = await result.get(timeout=60)
    print("✅ Final Output:", final)
    return final

if __name__ == "__main__":
    asyncio.run(main())
