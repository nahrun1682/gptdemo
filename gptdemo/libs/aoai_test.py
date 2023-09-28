#reference:https://python.langchain.com/docs/integrations/llms/azure_openai
import os
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

print(os.environ["AZURE_OPENAI_API_KEY"])
