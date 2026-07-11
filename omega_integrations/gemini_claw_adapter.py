# omega_integrations/gemini_claw_adapter.py
import os
import google.generativeai as genai
from openclaw.core import BaseAgent, ToolRegistry

class GeminiSuperAgent(BaseAgent):
    def __init__(self, api_key, model_name="gemini-1.5-pro", tools=[]):
        super().__init__()
        genai.configure(api_key=api_key)
        self.formatted_tools = self._convert_tools_to_gemini(tools)
        self.model = genai.GenerativeModel(
            model_name=model_name,
            tools=self.formatted_tools,
            system_instruction="Eres Ómega, un agente autónomo."
        )
        self.chat = self.model.start_chat(enable_automatic_function_calling=True)

    def _convert_tools_to_gemini(self, openclaw_tools):
        return [tool.to_gemini_format() for tool in openclaw_tools]

    def execute_turn(self, user_input):
        response = self.chat.send_message(user_input)
        return response.text
