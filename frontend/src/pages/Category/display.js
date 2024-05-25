import { useEffect, useState } from "react";
import { getCategoryProduct } from "../../Services/backend/product";
import ProductItem from "../../components/Product/User/ProductItem";

function Display() {
    const [display, setDisplay] = useState();

    useEffect(() => {
        const fetchAPI = async () => {
            const data = await getCategoryProduct('display');
            setDisplay(data);
            console.log(data);
        }
        fetchAPI();
    }, []);

    return (
        <>
            {display && (
                <div className="product">
                    {display.map((item, index) => (
                        <ProductItem item={item} />
                    ))}
                </div>
            )}
        </>
    )
}

export default Display;