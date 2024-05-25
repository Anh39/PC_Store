import { get, post, del, patch } from "./base";

export const getCart = async () => {
    const result = await get(`cart`)
    if (result != null) {
        const data = await result.json();
        return data;
    } else {
        return null;
    }
}
export const addProductToCart = async (id) => {
    let option = {
        'id': id
    }
    const result = await post(`cart`, option)
    if (result != null) {
        return true
    } else {
        return false
    }
}
export const changeCartAmount = async (id, amount) => {
    let option = {
        'id': id,
        'amount': amount
    }
    const result = await patch(`cart`, option)
    if (result != null) {
        return true
    } else {
        return false
    }
}
export const deleteCartProduct = async (id) => {
    const result = await del(`cart/?id=${id}`)
    if (result != null) {
        return true
    } else {
        return false
    }
}

export const deleteCartAll = async () => {
    const result = await del(`cart/?id=${-1}`)
    if (result != null) {
        return true
    } else {
        return false
    }
}
