import asyncio, os
from dotenv import load_dotenv
from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

async def main():
    load_dotenv()  # .env から GOOGLE_API_KEY を読み込む
    llm = ChatGoogleGenerativeAI(
        api_key=os.environ["GOOGLE_API_KEY"],
        model="gemini-2.0-flash"
    )
    agent = Agent(
        task="Google で ChatGPT と Bing を比較検索して結果を返して",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
