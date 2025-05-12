from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFacePipeline
from transformers import pipeline
import os

# Load prompt template from file
def load_prompt(template_name):
    with open(f"agents/prompts/{template_name}.txt", "r") as file:
        return file.read()

class CBTTherapist:
    def __init__(self, trauma_safe=False):
        template_name = "trauma_safe" if trauma_safe else "socratic"
        prompt_text = load_prompt(template_name)

        self.prompt = PromptTemplate.from_template(prompt_text)

        # Hugging Face LLM pipeline (you can switch models here)
        hf_pipeline = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1", max_new_tokens=200)
        llm = HuggingFacePipeline(pipeline=hf_pipeline)

        # LangChain LLM Chain
        self.chain = LLMChain(prompt=self.prompt, llm=llm)

    def chat(self, user_input):
        return self.chain.run({"user_input": user_input})
