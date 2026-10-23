from . import bypass_ssl  # <--- Use a dot (.) for relative package import


import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()

def main() -> None:
    information = """
    Irrfan Khan (Hindustani pronunciation: [ɪɾfɑːn xɑːn]; born Sahabzade Irfan Ali Khan; 7 January 1967 – 29 April 2020)[2] was an Indian actor who worked in Indian cinema as well as British and American films. Widely regarded as one of the finest actors in world cinema,[3][4] Khan's career spanned over 30 years and earned him numerous accolades, including a National Film Award, an Asian Film Award, and six Filmfare Awards. In 2011, he was awarded the Padma Shri, India's fourth highest civilian honour.[5] In 2021, he was posthumously awarded the Filmfare Lifetime Achievement Award.
    Khan made his film debut with a small role in Salaam Bombay! (1988), which was followed by years of struggle. He acted in a few Film and Television Institute of India student films such as Reconnaissance (1990), directed by Sandeep Chattopadhyay.[6][7] Among his first Hindi movies were Drishti (1990), a film by Govind Nihalani starring Dimple Kapadia and Shekhar Kapoor, in which he had a small but prominent role, and Ek Doctor Ki Maut (also in 1990), in which he portrayed a journalist and shared a major role opposite lead players Pankaj Kapur and Shabana Azmi. After this, he acted in the British film The Warrior (2001). He had his breakthrough as a leading actor in the Hindi movies Haasil (2003) and Maqbool (2004). He went on to gain critical acclaim for his roles in The Namesake (2006) for which he was nominated for the Independent Spirit Award for Best Supporting Male, Life in a... Metro (2007), and Paan Singh Tomar (2011). For portraying the title character in the last of these, he won the National Film Award for Best Actor. Further success came for his starring roles in The Lunchbox (2013), Piku (2015), and Talvar (2015) and he had supporting roles in the Hollywood films The Amazing Spider-Man (2012), Life of Pi (2012),[8] Jurassic World (2015), and Inferno (2016).[9][10] His other notable roles were in Slumdog Millionaire (2008), New York (2009), Haider (2014), and Gunday (2014), and the television series In Treatment (2010).[11][12] His highest-grossing Hindi film release came with the comedy-drama Hindi Medium[13] (2017), and his final film appearance was in its sequel Angrezi Medium (2020), both of which won him the Filmfare Award for Best Actor in 2018 and 2021.[14]
    As of 2017, his films had grossed $3.643 billion (₹237 billion) at the worldwide box office.[15] Khan was diagnosed with neuroendocrine cancer in March 2018,[16][17] and died from the disease on 29 April 2020.[2] Khan was described by Peter Bradshaw of The Guardian as "a distinguished and charismatic star in Hindi and English-language movies whose hardworking career was an enormously valuable bridge between South Asian and Hollywood cinema".[10] He was honoured in the 'In memoriam' segment of the 93rd Academy Awards.
    """
    summary_template = """
    Given the information {information} about a person I want you to create:
    1. A short summary 
    2. Two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    llm = ChatOpenAI(
        model = os.environ.get("DEPLOYMENT_NAME"),
        temperature = 0.7,
        api_key = os.environ.get("OPENAI_API_KEY"),
        base_url = os.environ.get("AZURE_OPENAI_ENDPOINT"),
        )

    #llm = ChatOllama(model = "llama3.2:latest", temperature = 0.3)
    
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
