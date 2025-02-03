from ..prompts import (
    get_shipping_time_estimator_prompt,
    get_competitor_price_comparison_prompt,
    get_discount_promo_checker_prompt,
    get_return_policy_checker_prompt,
    get_search_agg_prompt
)

from ..tool import (
    search_aggregator, 
    shipping_time_estimator, 
    competitor_price_comparison, 
    return_policy_checker, 
    discount_promo_checker
)

from autogen import (
    AssistantAgent, 
    UserProxyAgent, 
    register_function
)

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class FashonAgent:
    def __init__(self):
        self.chatbot, self.user_proxy = self._setup_agents()
        self._register_functions()

    def _setup_agents(self) -> tuple:
        """
        Set up the chatbot and user proxy agents.
        """
        chatbot = AssistantAgent(
            "chatbot",
            system_message="Reply TERMINATE when the task is done or when user's content is empty",
            llm_config={
                "model": "gpt-4o",
                "api_key": os.getenv("OPENAI_API_KEY")
            },
        )
        user_proxy = UserProxyAgent(
            name="User",
            is_termination_msg=lambda x: x.get("content", "") and "TERMINATE" in x.get("content", ""),
            human_input_mode="NEVER",
            code_execution_config={"use_docker": False},
        )
        return chatbot, user_proxy

    def _register_functions(self):
        """
        Register the necessary functions to the chatbot agent.
        """
        register_function(
            search_aggregator, 
            caller=self.chatbot, 
            executor=self.user_proxy, 
            name="search_aggregator", 
            description=get_search_agg_prompt()
        )
        register_function(
            shipping_time_estimator, 
            caller=self.chatbot, 
            executor=self.user_proxy, 
            name="shipping_time_estimator", 
            description=get_shipping_time_estimator_prompt()
        )
        register_function(
            discount_promo_checker, 
            caller=self.chatbot, 
            executor=self.user_proxy, 
            name="discount_promo_checker", 
            description=get_discount_promo_checker_prompt()
        )
        register_function(
            competitor_price_comparison, 
            caller=self.chatbot, 
            executor=self.user_proxy, 
            name="competitor_price_comparison", 
            description=get_competitor_price_comparison_prompt()
        )
        register_function(
            return_policy_checker, 
            caller=self.chatbot, 
            executor=self.user_proxy, 
            name="return_policy_checker", 
            description=get_return_policy_checker_prompt()
        )

    def execute_task(self, task: str):
        """
        Execute a task by initiating the chat through the user proxy.
        """
        response = self.user_proxy.initiate_chat(self.chatbot, message=task)
        return response

if __name__ == "__main__":
    # Create an instance of FashonAgent and execute a task.
    agent = FashonAgent()
    result = agent.execute_task(
        "I want to buy a cocktail dress from SiteB, but only if returns are hassle-free. Do they accept returns?"
    )
    print(result)
