import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

function Failure() {
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
                <h1>Thanh toán thất bại!</h1>
                <p>Chúc bạn thành công lần sau.</p>
            </div>
        </>
    )
}

export default Failure;