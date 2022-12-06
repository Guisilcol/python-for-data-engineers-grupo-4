import pydantic

class GetMethodResponseBodyModel(pydantic.BaseModel):
    database: list 
    ieee_api: list
    science_direct_api: list

class PostMethodRequestBodyModel(pydantic.BaseModel):
    pass