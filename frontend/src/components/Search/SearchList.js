/* eslint-disable react-hooks/exhaustive-deps */
import { useEffect, useState } from "react";
import { searchProductList } from "../../Services/backend/product";
import { Col, Row } from "antd";
import ProductItem from "../Product/User/ProductItem";

function SearchList(props) {
    const { data = [], onReload } = props;
    const [dataFinal, setDataFinal] = useState([]);

    useEffect(() => {
        const fetchAPI = async () => {
            onReload();
            let name = 'pc'
            const product = await searchProductList(name);

            const newData = data.map((item) => {
                const newItem = product.find((p) => p.id === item.id && p);
                return { ...newItem }
            });
            setDataFinal(newData);
        };
        fetchAPI();
    }, [data]);

    console.log(dataFinal);

    return (
        <>
            {dataFinal.length > 0 ? (
                <div className="product">
                    <Row gutter={[20, 20]}>
                        {dataFinal.map((item) => (
                            <Col span={6}>
                                <ProductItem item={item} key={item.id} />
                            </Col>
                        ))}
                    </Row>
                </div>
            ) : (
                <div className="mt-20">Không tìm thấy sản phẩm nào</div>
            )}
        </>
    )
}

export default SearchList;