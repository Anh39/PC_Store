from backend.server.api.product import ProductDBAPI
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from .api import DatabaseAPI
import heapq
from abc import abstractmethod
import pickle
from backend.common import folder_path

class BaseModel:
    def __init__(self) -> None:
        self.model = None
    @abstractmethod
    async def train(self) -> None:
        pass
    @abstractmethod
    async def save(self) -> None:
        pass
    @abstractmethod
    async def load(self) -> None:
        pass
    @abstractmethod
    async def predict(self,id : int,amount : int = 10) -> list[tuple[int,float]]:
        pass
class TFIDF:
    def __init__(self) -> None:
        self.data_api = DatabaseAPI()
        self.full_datas : dict[dict[str]] = None
        self.data_name = 'tfidf_data.pickle'
        self.model = TfidfVectorizer()
        self.model_name = 'tfidf_model.pickle'
        self.data_api.start()
    async def _get_data(self) -> list[str]:
        self.full_datas = await self.data_api.get_full_data()
        info_datas = []
        for key in self.full_datas:
            info_datas.append(self.full_datas[key]['info'])
        return info_datas
    @abstractmethod
    async def train(self,resue = True) -> None:
        if (resue):
            load_result = self.load()
            if (load_result):
                return
        data = await self._get_data()
        self.model.fit_transform(data)
        self.save()
    @abstractmethod
    def save(self) -> None:
        with open(folder_path.join(folder_path.AI.model,self.model_name),'wb') as file:
            pickle.dump(self.model, file)
        with open(folder_path.join(folder_path.AI.model,self.data_name),'wb') as file:
            pickle.dump(self.full_datas, file)
    @abstractmethod
    def load(self) -> None:
        try:
            with open(folder_path.join(folder_path.AI.model,self.model_name),'rb') as file:
                self.model = pickle.load(file)
            with open(folder_path.join(folder_path.AI.model,self.data_name),'rb') as file:
                self.full_datas = pickle.load(file)
            return True
        except:
            return False
    @abstractmethod
    def predict(self,id : int,amount : int = 10) -> list[tuple[int,float]]:
        if (self.model == None or self.full_datas == None):
            self.load()
        score = {}
        target_matrix = self.model.transform([self.full_datas[id]['info']])
        for key in self.full_datas:
            if (key != id):
                compare_matrix = self.model.transform([self.full_datas[key]['info']])
                score[key] = cosine_similarity(target_matrix,compare_matrix)[0][0]
        result = heapq.nlargest(amount,score.items(),key=lambda item : item[1])
        return result
