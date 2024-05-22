import { post } from "./base"

export const login = async (email, password) => {
    const option = {
        'email' : email,
        'password' : password
    }
    const result = await post('login',option)
    if (result != null) {
        const data = await result.json()
        return data
    } else {
        return {
            'success' : false,
            'token' : null,
            'role' : null // 'Customer' , 'Admin'
        }
    }
}
export const register = async (email, password,username = null) => {
    const option = {
        'email' : email,
        'password' : password,
        'username' : username // nullable
    }
    const result = await post('register',option)
    if (result != null) {
        const data = await result.json()
        return data
    } else {
        return {
            'success' : false,
            'token' : null,
            'role' : null // 'Customer'
        }
    }
}
