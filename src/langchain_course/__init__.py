import os

from dotenv import load_dotenv

load_dotenv()

def main() -> None:
    print("Hello from langchain-course!")
    print(os.environ.get("AZURE_FOUNDARY_OPENAI_ENDPOINT"))
    print(os.environ.get("MODEL"))



if __name__ == "__main__":
    main()



#uv run langchain-course
