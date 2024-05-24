import { useDispatch } from "react-redux";
import { deleteItem, updateQuantity } from "../../actions/cart";
import { useRef } from "react";
function CartItem(props) {
    const { item } = props;
    const inputRef = useRef();
    const dispatch = useDispatch();

    const handleDown = () => {
        if (item.quantity > 1) {
            dispatch(updateQuantity(item.id, -1));
            inputRef.current.value = parseInt(inputRef.current.value) - 1;
        }
    }

    const handleUp = () => {
        dispatch(updateQuantity(item.id));
        inputRef.current.value = parseInt(inputRef.current.value) + 1;
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
                    <button onClick={handleDown}>-</button>
                    <input ref={inputRef} defaultValue={item.quantity} />
                    <button onClick={handleUp}>+</button>
                </div>
                <button onClick={handleDelete}>Xóa</button>
            </div>
        </>
    )
}

export default CartItem;