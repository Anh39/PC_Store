import { useDispatch, useSelector } from "react-redux";
import CartList from "./CartList";
import { deleteAll } from "../../actions/cart";
import { Button } from "antd";
import { deleteCartAll } from "../../Services/backend/cart";
import { useEffect, useState } from "react";
import { getCart } from "../../Services/backend/cart";
import { createTransaction } from "../../Services/backend/transaction";

function Cart() {
    const [total, setTotal] = useState(0);
    const dispatch = useDispatch();
    const cartRedux = useSelector(state => state.cartReducer);
    const [reload, setReload] = useState(false);

    const fetchAPI = async () => {
        const data = await getCart();
        setCart(data);
        const temp = data.reduce((sum, item) => {
            const priceNew = item.price;
            return sum + priceNew * item.amount;
        }, 0);
        setTotal(temp);
    }

    const handleDeleteAll = async () => {
        console.log(cartRedux);
        dispatch(deleteAll());
        const response = deleteCartAll();
        if (response) {
            setReload(!reload);
            fetchAPI();
        } else {

        }
    }

    const [cart, setCart] = useState();

    useEffect(() => {
        fetchAPI();
    }, [total]);

    const handleReload = () => {
        fetchAPI();
    }

    const Payment = async () => {
        const response = await createTransaction();
        console.log(response);
        if (response) {
            window.location.href = response;
        }
    }

    return (
        <>
            <h2>Giỏ hàng</h2>
            <Button onClick={handleDeleteAll}>Xóa tất cả</Button>

            <div>
                {cart && cart.length > 0 ? (
                    <>
                        <CartList onReload={handleReload} onDelete={handleDeleteAll} />
                        <div className="cart__total">
                            Tổng tiền: <span>{total > 0 ? total : 0}đ</span>
                        </div>
                        <Button onClick={Payment}>Thanh toán</Button>
                    </>
                ) : (
                    <>giỏ trống</>
                )}
            </div>
        </>
    )
}

export default Cart;