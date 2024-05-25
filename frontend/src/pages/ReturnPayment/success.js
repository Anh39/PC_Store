import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

function Success() {
    const navigate = useNavigate();
    navigate("/");

    useEffect(() => {
        setTimeout(() => {
            navigate("/");
        }, 1500);
    }, [navigate]);

    return (
        <>
            <div>
                <h1>Thanh toán thành công!</h1>
                <p>Cảm ơn bạn đã mua hàng tại cửa hàng của chúng tôi.</p>
            </div>
        </>
    )
}

export default Success;