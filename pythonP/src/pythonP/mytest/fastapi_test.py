from enum import Enum
from typing import Any
from fastapi import FastAPI

apple:str = "QOO"

class ModelName(str, Enum):
    model01 = "model01"
    model02 = "model02"
    model03 = "model03"

class BasicMath:
    def __init__(self) -> None:
        pass
    def add(self, x:int, y:int)->int:
        return x+y


def fastapi_01()->FastAPI:
    app:FastAPI = FastAPI(
        title="PythonP Color API",
        description="CIE 1931",
        version="0.1.0"
    )
    
    @app.get("/")
    async def root()->dict[str, str]:
        return {"message": "Hello World"}
    
    @app.get("/items/{item_id}")
    async def read_item(item_id:str)->dict[str, str]:
        return {"item_id": item_id}
    @app.get("/qoo")
    async def test_func()->dict[str,str]:
        return {"test":"qoo"}
    @app.get("/users/me")
    async def get_user()->dict[str, str]:
        return {"users": apple}
    @app.get("/users/{user_id}")
    async def set_user(user_id:str)->dict[str, str]:
        global apple
        apple = user_id
        return {"user_id": apple}
    @app.get("/models/{model_name}") 
    async def get_model(model_name: ModelName)->dict[str, str]:
        if model_name is ModelName.model01:
            return {"model_name":model_name, "message":"model01"}
        elif model_name.value == "model02":
            return {"model_name":model_name, "message":"model02"}

        return {"model_name":model_name, "message":"model03"}
    @app.get("/file/{file_path:path}")
    async def read_file(file_path:str)->dict[str,str]:
        return {"file_path": file_path}

    @app.get("/items/")
    async def read_items(skip: int = 0, limit:int = 0)->list[dict[str,str]]:
        fake_items_db:list[dict[str,str]] = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
        return fake_items_db[skip:skip+limit]

    @app.get("/item_test/{item_id}")
    async def read_item_01(item_id:str, q:str|None = None)->dict[str,str]:
        if q:
            return {"item_id":item_id, "q":q}
        return {"item_id":item_id}

    @app.get("/items_test1/{item_id}")
    async def read_item_02(item_id:str, q:str | None=None, short:bool = False)->dict[str,str]:
        item:dict[str,str] = {"item_id":item_id}
        if q:
            item.update({"q":q})
        if not short:
            item.update({"description":"This is an amazing item that  has a long description"})

        return item
    @app.get('/items_test2/')
    async def read_item03(item_id:str, user_id:str,  q:str |None=None)->dict[str,str]:
        global apple
        item:dict[str,str] = {"item_id":apple}
        if q:
            item.update({"q":q})
        if user_id:
            item.update({"test": user_id})
        return item
    @app.get('/item_test3/{item_id}')
    async def read_item04(item_id:str, needy:str, skip:int, limit:int |None =None)->dict[str,str]:
        item:dict[str,Any] = {"item_id":item_id, "needy":needy, "skip":skip, "limit": limit}
        return item
    @app.get(path='/item_test4/add/{x}/{y}')
    async def read_item05(x:int, y:int)->dict[str,str]:
        bb:BasicMath = BasicMath()
        result:str = str(bb.add(x,  y))
        return {"x+y":result}
    @app.get(path='/item_test5/add/')
    async def item_test6(x:int, y:int)->dict[str,str]:
        bb:BasicMath = BasicMath()
        return {"x+y":str(bb.add(x,y))}

    return app

app:FastAPI = fastapi_01()
