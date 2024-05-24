import { useDispatch, useSelector } from "react-redux";
import CartList from "./CartList";
import { deleteAll } from "../../actions/cart";
import { Button } from "antd";

function Cart() {
    const dispatch = useDispatch();
    const cart = useSelector(state => state.cartReducer);

    const total = cart.reduce((sum, item) => {
        const priceNew = item.info.price;
        return sum + priceNew * item.quantity;
    }, 0);

    const handleDeleteAll = () => {
        dispatch(deleteAll());
    }

    return (
        <>
            <h2>Giỏ hàng</h2>
            <Button onClick={handleDeleteAll}>Xóa tất cả</Button>

            <div>
                {cart.length > 0 ? (
                    <>
                        <CartList />
                        <div className="cart__total">
                            Tổng tiền: <span>{total.toFixed(0)}đ</span>
                        </div>
                    </>
                ) : (
                    <>giỏ trống</>
                )}
            </div>
        </>
    )
}

export default Cart;