import os
from dotenv import load_dotenv
from autogen.agentchat.user_proxy_agent import UserProxyAgent
from autogen.agentchat.group.patterns.round_robin import RoundRobinPattern
from autogen import ConversableAgent, GroupChat, GroupChatManager

load_dotenv("AutoGen/.env")

def main():
    llm_config = {
        "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
        "base_url": os.getenv("AZURE_OPENAI_API_BASE"),
        "model": os.getenv("AZURE_OPENAI_API_MODEL"),
        "api_version": os.getenv("AZURE_OPENAI_API_VERSION"),
        "api_type": "azure",
    }

    pm_agent = ConversableAgent(
        name = "ProductManager",
        system_message="You are an experienced product manager with 8+ years of experience managing software products in high-growth startups. You excel at stakeholder collaboration, translating user needs into roadmap priorities, and balancing speed with quality. You believe in customer-centric product design and thrive in cross-functional environments. You will design and oversee product features, ensure user needs are met, and deliver a cohesive user experience that balances business viability and technical feasibility. Remember that you are a product manager and do not write code. You only decompose the feature as much as you can and pass to developers for implementation.",
        llm_config=llm_config
    )
    dev_agent = ConversableAgent(
        name = "Developer", 
        system_message="You are a senior software engineer named DevX. You were trained on thousands of GitHub repositories and have years of experience shipping production-grade code. You work best with clear specs but can reverse-engineer unclear requests when needed. You value clean, maintainable code and always leave things better than you found them.",
        llm_config=llm_config
    )

    user_agent = UserProxyAgent(
        name="user_agent",
        llm_config=llm_config,
        human_input_mode="ALWAYS"
    )

    groupChat = GroupChat(
        agents=[user_agent, pm_agent, dev_agent],
        messages=[],
        max_round=4,
        speaker_selection_method="round_robin",
        allow_repeat_speaker=False
    )

    groupChatManager = GroupChatManager(groupChat, llm_config=llm_config)
    
    result = user_agent.initiate_chat(groupChatManager, message="I need your help to write a hello world with Python.")
    for msg in result.human_input:
        print(msg)

if __name__ == "__main__":
    main()
