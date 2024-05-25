import { useDispatch, useSelector } from "react-redux";
import { deleteItem, updateQuantity } from "../../actions/cart";
// import { useRef, useState } from "react";
import { Button, InputNumber } from "antd";
import { changeCartAmount, deleteCartProduct } from "../../Services/backend/cart";
import { useEffect, useState } from "react";
function CartItem(props) {
    const { item, onReload } = props;
    const dispatch = useDispatch();
    const cartRedux = useSelector(state => state.cartReducer);

    const ChangeQuantity = async (value) => {
        // dispatch(updateQuantity(item.id, value));
        const response = await changeCartAmount(item.id, value);
        console.log(response);
        onReload();
    }

    const handleDelete = async () => {
        dispatch(deleteItem(item.id));
        const response = await deleteCartProduct(item.id);
        if (response) {
            onReload();
        }
    }

    return (
        <>
            <div className="cart__item" key={item.id}>
                <div className="cart__image">
                    <img src={item.thumbnail} alt={item.name} />
                </div>
                <div className="cart__content">
                    <h4 className="cart__tilte">{item.name}</h4>
                    <div className="cart__price-new">{item.price}đ</div>
                </div>
                <div className="cart__quantity">
                    <InputNumber min={1} defaultValue={item.amount} onChange={ChangeQuantity} />
                </div>
                <Button onClick={handleDelete}>Xóa</Button>
            </div>
        </>
    )
}

export default CartItem;