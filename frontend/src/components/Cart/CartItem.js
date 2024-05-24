import { useDispatch } from "react-redux";
import { deleteItem, updateQuantity } from "../../actions/cart";
// import { useRef, useState } from "react";
import { Button, InputNumber } from "antd";
function CartItem(props) {
    const { item } = props;
    const dispatch = useDispatch();

    // const handleDown = () => {
    //     if (item.quantity > 1) {
    //         dispatch(updateQuantity(item.id, -1));
    //         inputRef.current.value = parseInt(inputRef.current.value) - 1;
    //     }
    // }

    // const handleUp = () => {
    //     dispatch(updateQuantity(item.id));
    //     inputRef.current.value = parseInt(inputRef.current.value) + 1;
    // }

    const ChangeQuantity = (value) => {
        dispatch(updateQuantity(item.id, value));
    }

    const handleDelete = () => {
        dispatch(deleteItem(item.id));
    }

    return (
        <>
            <div className="cart__item" key={item.info.id}>
                <div className="cart__image">
                    <img src={item.info.thumbnail} alt={item.info.title} />
                </div>
                <div className="cart__content">
                    <h4 className="cart__tilte">{item.info.name}</h4>
                    <div className="cart__price-new">{item.info.price}đ</div>
                </div>
                <div className="cart__quantity">
                    <InputNumber min={1} defaultValue={1} onChange={ChangeQuantity} />
                </div>
                <Button onClick={handleDelete}>Xóa</Button>
            </div>
        </>
    )
}

export default CartItem;