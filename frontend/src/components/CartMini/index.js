import { Badge, Button } from "antd";
import { useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { ShoppingCartOutlined } from "@ant-design/icons";

function CartMini() {
    const cart = useSelector(state => state.cartReducer);
    const total = cart.length;

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