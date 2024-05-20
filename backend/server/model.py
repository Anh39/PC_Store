from pydantic import BaseModel

class ModifyLog(BaseModel):
    time : str
    by : str
    @classmethod
    def get_test(cls) -> 'ModifyLog':
        test = ModifyLog(time='12-4-2024',by='adminddd')
        return test
class PurchaseLog(BaseModel):
    time : str
    by : str
    amount : int
    total_cost : float
    @classmethod
    def get_test(cls) -> 'PurchaseLog':
        test = PurchaseLog(time='22-5-2024',by='whoknow',amount=238123,total_cost=23892.23)
        return test
class Item(BaseModel):
    name : str
    price : float
    info : dict[str,object]
    modified_log : list[ModifyLog]
    purchased_by : list[PurchaseLog]
    metadata : dict[str,object]
    @classmethod
    def get_test(cls) -> 'Item':
        test = Item(name='Chicken',
                    price=232.2,
                    info={'aa':'bb'},
                    modified_log=[ModifyLog.get_test()],
                    purchased_by=[PurchaseLog.get_test()],
                    metadata={'hell':1})
        return test
class PaymentMethod(BaseModel):
    name : str
    # More
    @classmethod
    def get_test(cls) -> 'PaymentMethod':
        test = PaymentMethod(name='hmmmm')
        return test

class ListItem(BaseModel):
    items : list[Item]
    metadatas : list[dict[str,object]]
    @classmethod
    def get_test(cls) -> 'ListItem':
        test = ListItem(items=[Item.get_test()],
                        metadatas=[{'a':'g'}])
        return test
class Basket(ListItem):
    voucher : list['Voucher']
    @classmethod
    def get_test(cls) -> 'Basket':
        test = Basket(items=[Item.get_test()],
                        metadatas=[{'a':'g'}],
                        voucher=[Voucher.get_test()])
        return test
class ListVoucher(BaseModel):
    vouchers : list['Voucher']
    metadatas : list[dict[str,object]]
    @classmethod
    def get_test(cls) -> 'ListVoucher':
        test = ListVoucher(vouchers=[Voucher.get_test()],
                           metadatas=[{'a':'g'}])
        return test
class Voucher(BaseModel):
    id : str
    percent_discount : float
    source : str | None = None
    description : str | None = None
    categories_apllied : list = ['all']
    received_date : str
    expire_date : str
    @classmethod
    def get_test(cls) -> 'Voucher':
        test = Voucher(id='123',
                       percent_discount=15.2,
                       source='admin:))',
                       description='nothing here',
                       categories_apllied=['all'],
                       received_date='2-4-2045',
                       expire_date='1-4-2022')
        return test
class UserInfo(BaseModel):
    name : str
    password : str
    gender : str | None = None
    age : int | None = None
    birthday : str | None = None
    phone : str | None = None
    email : str | None = None
    address : str | None = None
    paymentmethods : list[PaymentMethod] = []
    description : str | None = None
    @classmethod
    def get_test(cls) -> 'UserInfo':
        test = UserInfo(name='abc',
                        password='123',
                        gender='Male',
                        age='12',
                        birthday='4-12-2003',
                        phone='0123456789',
                        email='abc@gmail.com',
                        address='12-sw-2d-33ddd',
                        paymentmethods=[PaymentMethod.get_test()],
                        description='hello')
        return test
class UserInfoShort(BaseModel):
    name : str
    description : str | None = None
    @classmethod
    def get_test(cls) -> 'UserInfoShort':
        test = UserInfoShort(name='abc',
                             description=':))')
        return test
class UserItem(BaseModel):
    basket : Basket
    liked_item : ListItem
    blacklist_item : ListItem
    wishlish_item : ListItem
    delivering : ListItem
    purchased : ListItem
    voted : ListItem
    voucher : ListVoucher
    @classmethod
    def get_test(cls) -> 'UserItem':
        test = UserItem(basket=Basket.get_test(),
                        liked_item=ListItem.get_test(),
                        blacklist_item=ListItem.get_test(),
                        wishlish_item=ListItem.get_test(),
                        delivering=ListItem.get_test(),
                        purchased=ListItem.get_test(),
                        voted=ListItem.get_test(),
                        voucher=ListVoucher.get_test())
        return test

class BaseUser(BaseModel):
    token : str
    @classmethod
    def get_test(cls) -> 'BaseUser' :
        test = BaseUser(token='123712983ujklfsja')
        return test
class Guest(BaseUser):
    pass
class User(BaseUser):
    id : str
    info : UserInfo
    item : UserItem | None = None
    @classmethod
    def get_empty(cls) -> 'User':
        pass
    @classmethod
    def get_test(cls) -> 'User':
        test = User(id='nekdawnkk',
                    token='123712983ujklfsja',
                    info=UserInfo.get_test(),
                    item=UserItem.get_test())
        return test
class UserShort(BaseModel):
    id : str
    info : UserInfoShort
    @classmethod
    def get_test(cls) -> 'UserShort':
        test = UserShort(id='123yhj',
                             info=UserInfoShort.get_test())
        return test
class Admin(BaseUser):
    id : str
    info : UserInfoShort
    @classmethod
    def get_test(cls) -> 'Admin':
        test = Admin(id='djwalksdnjjawhr89212y98yhbdjagt ybyauygfaj3ymnr9q9j983mrntqauinfbawe',
                     info=UserInfoShort.get_test())
        return test
    
class InfoChangeUnit(BaseModel):
    key : str
    old : object
    new : object
    @classmethod
    def get_test(cls) -> 'InfoChangeUnit':
        test = InfoChangeUnit(key='name',old='a',new='b')
        return test