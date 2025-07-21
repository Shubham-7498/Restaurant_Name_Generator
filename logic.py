from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama2")

name_prompt = PromptTemplate(
    input_variables=["cuisine"],
    template="I want to open a restaurant for {cuisine} food. Suggest only one fancy and catchy name for this without any description or additional text",
)

name_chain = name_prompt |llm 

menu_prompt = PromptTemplate(
    input_variables=["restaurant_name"],
    template="""A suggested simple menu for the restaurant named {restaurant_name} without any response text.
    List only the dish names without any description or additional text.""",
)
menu_chain = menu_prompt | llm

def generate_menu(cuisine):
    name = name_chain.invoke({"cuisine": cuisine}).strip()
    menu = menu_chain.invoke({"restaurant_name": name}).strip()
    return {
        "restaurant_name": name,
        "menu": menu
    }