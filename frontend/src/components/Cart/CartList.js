/* eslint-disable react-hooks/exhaustive-deps */
import "./CartList.scss";
import CartItem from "./CartItem";
import { useEffect, useState } from "react";
import { getCart } from "../../Services/backend/cart";

function CartList(props) {
    const { onReload } = props;
    // const cart = useSelector(state => state.cartReducer);

    const [cart, setCart] = useState();

    useEffect(() => {
        const fetchAPI = async () => {
            const data = await getCart();
            setCart(data);
            onReload();
        }

        fetchAPI();
    }, [cart]);

    return (
        <>
            <div className="cart">
                {cart && (cart.map(item => (
                    <CartItem item={item} onReload={onReload} />
                )))}
            </div>
        </>
    )
}

export default CartList;