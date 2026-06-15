import os
from groq import Groq
from django.conf import settings

class MultiAgentOrchestrator:
    def __init__(self):
        # Fallback to an empty string if key isn't loaded yet to prevent initialization crashes
        api_key = os.getenv("GROQ_API_KEY", "")
        self.client = Groq(api_key=api_key)
        self.model = "llama3-70b-8192" # Ultra-fast, highly accurate open-weights model on Groq

    def execute_agentic_workflow(self, engineer_query: str, context_chunks: list, current_metrics: dict) -> str:
        """
        Executes a composite Agentic Workflow routing across specialized prompt schemas 
        acting as specialized industrial personas.
        """
        # Synthesize retrieval chunks
        retrieved_context = "\n".join(context_chunks) if context_chunks else "No specific manuals found matching system signatures."
        
        # System instructions enforcing the multi-agent persona layout
        system_prompt = f"""
        You are an expert Multi-Agent AI system running industrial SCADA analysis loops for a Steel Manufacturing Plant.
        Your current operational parameters:
        [LIVE TELEMETRY]: {current_metrics}
        [RETRIEVED KNOWLEDGE SPECIFICATION]: {retrieved_context}

        Execute instructions across these sub-agents sequentially:
        1. [Diagnosis Agent]: Calculate structural or physical root causes (e.g., thermal fatigue, bearing wear, cavitation) based on telemetry deviations.
        2. [Risk Agent]: Map structural degradation to structural down-time impacts.
        3. [Recommendation Agent]: Issue clear, itemized, action-oriented items adhering strictly to safety guidelines.

        Respond back in a highly professional, scannable industrial layout using dark operations styling markup blocks.
        """

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": engineer_query}
            ],
            temperature=0.2
        )
        return completion.choices[0].message.content