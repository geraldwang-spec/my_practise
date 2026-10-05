import asyncio
import os
import json
from socket import timeout
from flask import request
import requests
from groq import AsyncGroq
from flask.cli import load_dotenv
from pydantic_core.core_schema import FieldPlainInfoSerializerFunction
from requests.utils import dict_from_cookiejar
from urllib3 import response
from modules.utils import MessageResponse

class LLMApiController:
    __groq_api:str | None
    __client:AsyncGroq
    __messages:list
    __tools: list
    __ai_model = "openai/gpt-oss-20b"

    def __init__(self) -> None:
        _ = load_dotenv()
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            raise ValueError("未找到 GROQ_API_KEY 設定")
        self.__groq_api= api_key
        self.__client = AsyncGroq(api_key=self.__groq_api)
        self.__messages = []
        self.__tools= [
            {
                 "type": "function",
                 "function": {
                     "name": "get_weather",
                     "description": "查詢特定地點的天氣狀況",
                     "parameters": {
                         "type": "object",
                         "properties": {
                             "location": {
                                 "type": "string",
                                 "description": "地點的英文名稱（例如：taipei、tokyo、new york），請將使用者輸入的中文地名轉換為對應的英文地名",
                             },
                         },
                         "required": ["location"],  # 宣告 location 為必填參數
                     },
                 },
            },
            {

            }]

    async def get_weather(self, location:str)->dict[str, str]:
        """
        呼叫 wttr.in 的公開 API 獲取天氣資訊 (免 API Key)。
        format=j1 會回傳 JSON 格式的數據。
        """
        url = f"https://wttr.in/{location}?format=j1"
        print(f"location = {location}")
        try:
            response = await asyncio.to_thread(requests.get, url, timeout=5)
            response.raise_for_status()
        except requests.RequestException:
            return {"error":"無法取得天氣數據"}
        
        data = response.json()
        current_condition = data.get("current_condition", [{}])[0]
        return current_condition

    async def product_data(product_id:int)->dict[str,str]:
        url = f"https://fakestoreapi.com/products/{product_id}"
        print(f"product_id={product_id}")
        try:
            response = await asyncio.to_thread(requests.get, url, timeout=5)
            response.raise_for_status()
        except requests.RequestException:
            return {"error":"找不到該產品"}

        data = response.json()
        current_condition = data.get("current_condition", [{}])[0]
        return current_condition

    async def receive_message(self, user_input)-> MessageResponse:
        assert self.__ai_model is not None, "__ai_model should be init"
        assert self.__client is not None, "__client should be init"
        finial_content = ""
        self.__messages.append({"role": "user", "content": user_input})
        response = await self.__client.chat.completions.create(
            model=self.__ai_model,  # 支援工具呼叫的高效 Groq 模型
            messages=self.__messages,
            tools=self.__tools,
            tool_choice="auto")

        res_mesg = response.choices[0].message
        self.__messages.append(res_mesg)

        print(f"res_mesg = {res_mesg.tool_calls}")

        if res_mesg.tool_calls:
            for tool_call in res_mesg.tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                if function_name == "get_weather":
                    result = await self.get_weather(location = function_args.get("location"))
                    print(f"{result}")
                    
                    self.__messages.append({
                        "role":"tool",
                        "tool_call_id":tool_call.id,
                        "content": json.dumps(result, ensure_ascii=False)})

                    self.__messages.append(
                            {
                                 "role": "system",
                                 "content": (
                                     "你是一位專業的個人穿搭與旅遊顧問。"
                                     "以下是系統剛剛從氣象局 API 抓取到的即時天氣數據：\n"
                                     f"地點：{function_args.get("location")}\n"
                                     f"數據：{json.dumps(result, ensure_ascii=False)}\n\n"
                                     "請根據這些數據（例如氣溫 temp_C、天氣描述 weatherDesc 等），"
                                     "用『繁體中文』回答使用者的問題，並給出具體、貼心的建議。"
                                 )
                             })

                # elif function_name == "product_data":



            res_mesg2 = await self.__client.chat.completions.create(
                model=self.__ai_model,
                messages=self.__messages,
                temperature=0.6, # 稍微降低一點隨機性，讓穿搭建議更合理
                max_tokens=512)
            finial_content = res_mesg2.choices[0].message.content
            self.__messages.append({"role":"assistant", "content": finial_content })
        else:
            finial_content = res_mesg.content

        return MessageResponse(success=True, message=finial_content, data=None)

    
