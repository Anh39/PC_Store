import { useDispatch, useSelector } from "react-redux";
import { addToCart } from "../../../actions/cart";
import { Card } from "antd";
import { Link, useNavigate } from "react-router-dom";
import "./DisplayProduct.scss";

function ProductItem(props) {
    const { item } = props;
    const navigate = useNavigate();

    const dispatch = useDispatch();
    const cart = useSelector(state => state.cartReducer);

    const handleAddToCart = () => {
        if (cart.some(itemCart => itemCart.id === item.id)) {
            // dispatch(updateQuantity(item.id));
        } else {
            dispatch(addToCart(item.id, item));
        }
    }

    const ToDetail = () => {
        navigate(`/product/${item.id}`)
    }

    return (
        <>
            <div className="product__cart">
                <Card
                    hoverable
                    bordered={false}
                    size="small"
                    cover={<img className="product__image" src={item.thumbnail} alt={item.title} onClick={ToDetail} />}
                >
                    <h4 className="product__title" onclick={ToDetail}><Link to={`/product/${item.id}`}>{item.title}</Link></h4>
                    <div className="product__price-new">
                        {(item.price * (100 - item.discountPercentage) / 100).toFixed(0)}$
                    </div>
                    <div className="product__price-old">{item.price}$</div>
                    <div className="product__percent">{item.discountPercentage}%</div>
                    <button onClick={handleAddToCart}>Thêm vào giỏ hàng</button>
                </Card>
            </div>
        </>
    )
}

export default ProductItem;