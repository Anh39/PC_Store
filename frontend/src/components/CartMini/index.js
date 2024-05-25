/* eslint-disable react-hooks/exhaustive-deps */
import { Badge, Button } from "antd";
import { useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { ShoppingCartOutlined } from "@ant-design/icons";
import { useEffect, useState } from "react";
import { getCart } from "../../Services/backend/cart";

function CartMini() {
    const cart = useSelector(state => state.cartReducer);
    const [total, setTotal] = useState(0);
    const [reload, setReload] = useState(false);

    useEffect(() => {
        const fetchAPI = async () => {
            const data = await getCart();
            let temp = data.length > 0 ? data.length : 0;
            setTotal(temp);
            setReload(!reload);
        }

        fetchAPI();
    }, [cart]);

    return (
        <>
            <NavLink to="cart" className={"navLinkActive"}>
                <Badge count={total}>
                    <Button type="text" icon={<ShoppingCartOutlined style={{fontSize: 30, color: "red"}} />}>
                    </Button>
                </Badge>
            </NavLink>
        </>
    )
}

export default CartMini;