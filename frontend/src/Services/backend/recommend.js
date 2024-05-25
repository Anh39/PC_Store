import { get} from "./base";

export const recommendProduct = async (id,limit = 8) => {
    // const result = await get("category");
    const result = await get(`recommend/?id=${id}&limit=${limit}`);
    if (result != null) {
        let data = await result.json();
        return data;
    } else {
        return []
    }
}