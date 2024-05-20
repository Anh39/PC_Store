from pydantic import BaseModel

class ModelReturn(BaseModel):
    name : str
    price : tuple[float,float] = [0,999999999]
    info : dict[str,object] 
    @classmethod
    def get_test(cls) -> 'ModelReturn':
        test = ModelReturn(name='pipi',
                           price=(0,12323232),
                           info={'w':':)'})
        return test