import asyncio
from flask import Blueprint, request
from llmapi import llmapi_controller
from modules.utils import MessageResponse
from llmapi.llmapi_controller import LLMApiController as llmapiC


def create_llmapi()->Blueprint:
    mName:str = "llmapi"
    llmapi_bp = Blueprint(mName, __name__, url_prefix=f"/{mName}")
    llmC: llmapiC = llmapiC()

    @llmapi_bp.route('/messageInput', methods=['POST', "GET"])
    def messageInput():
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return MessageResponse(
                success=False,
                message="無效JSON格式",
                data=None).to_response()

        print(f"data = {data.get("message")}")

        result = asyncio.run(llmC.receive_message(data.get("message")))

        return result.to_response()
        # return MessageResponse(success=True, message="iiii", data=None).to_response()
       
    return llmapi_bp
