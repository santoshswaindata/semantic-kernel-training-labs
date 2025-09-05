import asyncio
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.azure.chat_completion import AzureChatCompletion
from semantic_kernel.prompt_template.input_variable import InputVariable
from semantic_kernel.contents.chat_history import ChatHistory
from finance_plugin import FinanceAnalysisPlugin
from finance_prompts import FinancePrompts
from finance_filters import financial_approval_filter

async def main():
    # TODO: Initialize kernel with Azure OpenAI
    # TODO: Add finance plugin to kernel
    # TODO: Register security filter
    # TODO: Create chat history
    # TODO: Implement interactive conversation loop

    print("🏦 Welcome to your AI Financial Assistant!")
    print("I can help you analyze expenses, create budgets, and provide investment advice.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        # TODO: Process user input and generate response
        # TODO: Handle different types of financial queries
        # TODO: Apply appropriate templates and functions

    print("Thank you for using the AI Financial Assistant!")

if __name__ == "__main__":
    asyncio.run(main())