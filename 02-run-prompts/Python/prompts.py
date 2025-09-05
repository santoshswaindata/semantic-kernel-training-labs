import os
import asyncio
from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.functions.kernel_arguments import KernelArguments
from semantic_kernel.prompt_template import KernelPromptTemplate, HandlebarsPromptTemplate, PromptTemplateConfig

async def main():

    load_dotenv()
    # Set your values in the .env file
    api_key = os.getenv("PROJECT_KEY")
    endpoint = os.getenv("PROJECT_ENDPOINT")
    deployment_name = os.getenv("DEPLOYMENT_NAME")

    # Create a kernel with Azure OpenAI chat completion
    kernel = Kernel()
    chat_completion = AzureChatCompletion(
     api_key=api_key,
     endpoint=endpoint,
     deployment_name=deployment_name
    )
    kernel.add_service(chat_completion)

    # Create the chat history
    chat_history = ChatHistory()

    async def get_reply():
        # Get the reply from the chat completion service
        reply = await chat_completion.get_chat_message_content(
            chat_history=chat_history,
            kernel=kernel,
            settings=AzureChatPromptExecutionSettings()
        )
        print("Assistant:", reply)
        chat_history.add_assistant_message(str(reply))    

    # Create a semantic kernel prompt template
    sk_prompt_template = KernelPromptTemplate(
        prompt_template_config=PromptTemplateConfig(
            template="""
            You are a helpful career advisor. Based on the users's skills and interest, suggest up to 5 suitable roles.
            Return the output as JSON in the following format:
            "Role Recommendations":
            {
            "recommendedRoles": [],
            "industries": [],
            "estimatedSalaryRange": ""
            }

            My skills are: . My interests are: . What are some roles that would be suitable for me?
            """,
            name="recommend_roles_prompt",
            template_format="semantic-kernel",
        )
    )

    # Render the Semanitc Kernel prompt with arguments
    sk_render_prompt = await sk_prompt_template.render(
         kernel,
         KernelArguments(
              skills="Software Engineer, C#, Python, Drawing, Guitar, Dance",
              interests="Education, Psychology, Programming, Helping Others"
         )
    )

    # Add the Semanitc Kernel prompt to the chat history and get the reply
    chat_history.add_user_message(sk_render_prompt)
    await get_reply()
    # Create a handlebars template
    hb_prompt_template = HandlebarsPromptTemplate(
    prompt_template_config=PromptTemplateConfig(
         template="""
         <message role="system">
         Instructions: You are a career advisor. Analyze the skill gap between 
         the user's current skills and the requirements of the target role.
         </message>
         <message role="user">Target Role: </message>
         <message role="user">Current Skills: </message>

         <message role="assistant">
         "Skill Gap Analysis":
         {
             "missingSkills": [],
             "coursesToTake": [],
             "certificationSuggestions": []
         }
         </message>
         """,
         name="missing_skills_prompt",
         template_format="handlebars",
        )
    )

    # Render the Handlebars prompt with arguments
    hb_rendered_prompt = await hb_prompt_template.render(
     kernel,
     KernelArguments(
         targetRole="Game Developer",
         currentSkills="Software Engineering, C#, Python, Drawing, Guitar, Dance"
        )
    )

    # Add the Handlebars prompt to the chat history and get the reply
    chat_history.add_user_message(hb_rendered_prompt)
    await get_reply()

    # Get a follow-up prompt from the user
    print("Assistant : How can I help you?")
    user_input = input("User: ")

    # Add the user input to the chat history and get the reply
    chat_history.add_user_message(user_input)
    await get_reply()

if __name__ == "__main__":
        asyncio.run(main())