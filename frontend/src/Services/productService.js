import { del, get, patch, post } from "../utils/request";

export const getProductList = async () => {
    const result = await get("products");
    return result;
}

export const getProductDetail = async (id) => {
    const result = await get(`products/${id}`);
    return result;
}

export const createProduct = async (option) => {
    const result = await post("products", option);
    return result;
}

export const deleteProduct = async (id) => {
    const result = await del(`products/${id}`);
    return result;
}

export const editProduct = async (id, option) => {
    const result = await patch(`products/${id}`, option);
    return result;
}