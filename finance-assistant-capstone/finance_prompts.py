from semantic_kernel.prompt_template import PromptTemplateConfig, KernelPromptTemplate
from semantic_kernel.prompt_template.handlebars import HandlebarsPromptTemplate

class FinancePrompts:
    @staticmethod
    def get_expense_analysis_template():
        """Semantic Kernel template for expense analysis"""
        return KernelPromptTemplate(
            prompt_template_config=PromptTemplateConfig(
                template="""
You are a professional financial advisor. Analyze the provided expense data and create insights.

Expense Data: {{$expense_data}}
Monthly Income: {{$monthly_income}}

Provide analysis in this JSON format:
{
  "spending_summary": {
    "total_expenses": 0,
    "top_categories": [],
    "percentage_of_income": 0
  },
  "insights": {
    "highest_spending_category": "",
    "potential_savings_areas": [],
    "spending_patterns": ""
  },
  "recommendations": []
}
""",
                name="expense_analysis_prompt",
                template_format="semantic-kernel"
            )
        )

    @staticmethod
    def get_investment_advice_template():
        """Handlebars template for investment recommendations"""
        return HandlebarsPromptTemplate(
            prompt_template_config=PromptTemplateConfig(
                template="""
<message role="system">
You are a certified financial planner. Provide investment recommendations based on the user's profile.
</message>
<message role="user">
User Profile: {{userProfile}}
Available Investment Amount: ${{investmentAmount}}
</message>
<message role="assistant">
{
  "investment_recommendations": {
    "recommended_allocation": {},
    "expected_annual_return": "",
    "risk_level": "{{riskTolerance}}",
    "investment_options": []
  },
  "timeline_recommendations": {
    "short_term": "",
    "medium_term": "",
    "long_term": ""
  }
}
</message>
""",
                name="investment_advice_prompt",
                template_format="handlebars"
            )
        )