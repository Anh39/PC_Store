import { getCookie } from "../helpers/cookie";
const API_DOMAIN = "http://localhost:3000/"; // đổi tại đây

export const get = async (path) => {
    const response = await fetch(API_DOMAIN + path,{
        method: "GET",
        headers: {
            "Token" : getCookie('token')
        }
    });
    if (response.ok) {
        return response;
    } else {
        return null;
    }
};

export const post = async (path, option) => {
    const response = await fetch(API_DOMAIN + path, {
        method: "POST",
        headers: {
            "Token" : getCookie('token'),
            Accept: "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify(option)
    });
    if (response.ok) {
        return response;
    } else {
        return null;
    }
};

export const del = async (path) => {
    const response = await fetch(API_DOMAIN + path, {
        method: 'DELETE',
        headers: {
            "Token" : getCookie('token'),
        }
    });
    if (response.ok) {
        return response;
    } else {
        return null;
    }
}

export const patch = async (path, option) => {
    const response = await fetch(API_DOMAIN + path, {
        method: "PATCH",
        headers: {
            "Token" : getCookie('token'),
            Accept: "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify(option)
    });
    if (response.ok) {
        return response;
    } else {
        return null;
    }
}