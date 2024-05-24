import { get,post,del} from "./base";

export const getCart = async () => {
    const result = await get(`cart`)
    if (result != null) {
        const data = await result.json();
        return data;
    } else {
        return []
    }
}
export const addProductToCart = async (id) => { 
    let option = {
        'id' : id
    }
    const result = await post(`cart`,option)
    if (result != null) {
        return true
    } else {
        return false
    }
}
export const increaseAmount = async (id) => { 
    let option = {
        'id' : id,
        'command' : '+'
    }
    const result = await post(`cart`,option)
    if (result != null) {
        return true
    } else {
        return false
    }
}
export const decreaseAmount = async (id) => { 
    let option = {
        'id' : id,
        'command' : '-'
    }
    const result = await post(`cart`,option)
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