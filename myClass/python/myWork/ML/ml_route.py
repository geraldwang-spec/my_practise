
import asyncio
from flask import Blueprint, Response, request
from pandas.core import methods
from modules.utils import MessageResponse
from ML.linearRegression import ml_example as ml


def create_mlapi()->Blueprint:
    mName:str = "mlapi"
    mlapi_bp = Blueprint(mName, __name__, url_prefix=f"/{mName}")

    @mlapi_bp.route('/selectitem', methods=['POST', "GET"])
    def messageInput():
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return MessageResponse(
                success=False,
                message="無效JSON格式",
                data=None).to_response()

        print(f"data = {data.get("message")}")

        return MessageResponse(success=True, message="iiii", data=None).to_response()

    @mlapi_bp.route('/linearRegression', methods=['POST'])
    def linearRegression_example():
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return MessageResponse(
                success=False,
                message="無效JSON格式",
                data=None).to_response()
        
        points = data.get("points", [])
        if len(points) < 2:
            return MessageResponse(
                success=False,
                message="Need to 2 data points",
                data=None
            ).to_response()

        ml_ex:ml = ml()

        return ml_ex.process_linear_data(points=points).to_response()

    # @mlapi_bp.route('/gradientStep', methods=['POST'])
    # def gradientStep_example()->Response:
        
       
    return mlapi_bp
