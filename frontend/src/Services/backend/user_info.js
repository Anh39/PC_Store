import { get, del, patch } from "./base";

export const get_user_info = async () => {
    const result = await get('user')
    if (result != null) {
        const data = await result.json();
        return data;
    } else {
        return {
            "email": null,
            "name": null,
            "birthday": null,
            "phone": null,
            "gender": null,
            "address": null,
            "avatar": null,
            "card": null
        }
    }
}
export const change_user_info = async (confirm_password, change_data) => {
    const data = {
        "confirm_password": confirm_password,
        "data": {
            "password": change_data
        }
    } // add change data here , even password
    const result = await patch('user', data)
    if (result) {
        return true;
    } else {
        return false;
    }
}
export const delete_user = async (confirm_password) => {
    const data = {
        "confirm_password": confirm_password
    }
    const result = await del('user', data)
    if (result.ok) {
        return true;
    } else {
        return false;
    }
}

