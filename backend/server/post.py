from .model import *

class PostManager:
    def __init__(self) -> None:
        self.database = None
    async def create_post(self,data : dict) -> Post:
        return Post.get_test()
    async def search_posts(self,data : dict) -> list[Post]:
        return [Post.get_test()]
    async def get_post(self,data : dict) -> Post:
        return Post.get_test()
    async def recommend_posts(self,data : dict) -> list[Post]:
        return [Post.get_test()]
    async def change_post(self,data : dict) -> Post:
        return Post.get_test()
    async def delete_post(self,data : dict) -> bool:
        return True