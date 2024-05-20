import { get, patch, post } from "../utils/request";

export const login = async (email, password="") => {
    let pass = "";
    if (password !== "") {
        pass = `&password="${password}`;
    }
    const result = await get(`company?email=${email}&password=${pass}`);
    return result;
}

export const checkExit = async (type, value) => {
    const result = await get(`company?${type}=${value}`);
    return result;
}

export const createCompany = async (options) => {
    const result = await post("company", options);
    return result;
}

export const getDetailCompany = async (id) => {
    const result = await get(`company/${id}`);
    return result;
}

export const editCompany = async (id, options) => {
    const result = await patch(`company/${id}`, options);
    return result;
}