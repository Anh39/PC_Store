import { get} from "./base";

export const createTransaction = async () => {
    const result = await get(`transaction/create`)
    if (result != null) {
        const data = await result.json();
        const redirect_url = data.approval_url; // chuyển đến link này
        return data;
    } else {
        return []
    }
}

export const getHistory = async () => {
    const result = await get(`orders`)
    if (result != null) {
        const data = await result.json();
        return data;
    } else {
        return []
    }
}