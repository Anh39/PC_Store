import { useDispatch, useSelector } from "react-redux";
import { addToCart } from "../../../actions/cart";
import { Link, useNavigate } from "react-router-dom";
import "./DisplayProduct.scss";
import { Button } from "antd";
import { addProductToCart } from "../../../Services/backend/cart";

function ProductItem(props) {
    const { item } = props;
    const navigate = useNavigate();

    const dispatch = useDispatch();
    const cart = useSelector(state => state.cartReducer);

    const handleAddToCart = async () => {
        if (cart.some(itemCart => itemCart.id === item.id)) {
            alert("sản phẩm đã được thêm vào giỏ từ trước");
        } else {
            dispatch(addToCart(item.id, item));
            const response = await addProductToCart(item.id);
            console.log(response);
        }
    }

    const ToDetail = () => {
        navigate(`/product/${item.id}`);
    }

    return (
        <>
            <div className="product__item" key={item.index}>
                <div>
                    <img className="product__img" src={item.thumbnail} alt={item.title} onClick={ToDetail} />
                    <h4 className="product__title"> <Link to={`/product/${item.id}`}>{item.name}</Link></h4>
                </div>
                <div>
                    <div className="product__price-new">{item.price}đ</div>
                    <div className="product__price-old">{item.full_price}</div>
                    <Button onClick={handleAddToCart} className="product__button">Thêm vào giỏ hàng</Button>
                </div>
            </div>
        </>
    )
}

export default ProductItem;