from .model import *

class VoucherManager:
    def __init__(self) -> None:
        self.database = None
    async def create_voucher(self,data : dict) -> Voucher:
        return Voucher.get_test()
    async def search_vouchers(self,data : dict) -> list[Voucher]:
        return [Voucher.get_test()]
    async def get_voucher(self,data : dict) -> Voucher:
        return Voucher.get_test()
    async def recommend_vouchers(self,data : dict) -> list[Voucher]:
        return [Voucher.get_test()]
    async def change_voucher(self,data : dict) -> Voucher:
        return Voucher.get_test()
    async def delete_voucher(self,data : dict) -> bool:
        return True