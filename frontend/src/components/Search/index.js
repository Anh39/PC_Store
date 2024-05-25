/* eslint-disable no-unused-vars */
/* eslint-disable react-hooks/exhaustive-deps */
import { useEffect, useState } from "react";
import { useParams, useSearchParams } from "react-router-dom";
import { getSearch } from "../../Services/backend/product";
import { Tag } from "antd";
import SearchList from "./SearchList";
import "../Product/User/DisplayProduct.scss";
import ProductItem from "../Product/User/ProductItem";

function Search() {
    const { keyword } = useParams();
    const [searchParams, setSearchParams] = useSearchParams();
    const [data, setData] = useState();
    const keywordSearch = searchParams.get("keyword") || '';

    const fetchAPI = async () => {
        const response = await getSearch(keyword.toUpperCase());
        if (response) {
            setData(response);
        }

    };

    useEffect(() => {
        fetchAPI();
    }, [keyword]);

    const Reload = () => {
        fetchAPI();
    }

    return (
        <>
            <div>
                <strong>Kết quả tìm kiếm:</strong>
            </div>
            {data && (
                <div className="product">
                    {data && (data.map((item, index) => (
                        <ProductItem item={item} />
                    )))}
                </div>
            )}
        </>
    )
}

export default Search;