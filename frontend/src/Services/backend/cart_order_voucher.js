import { get} from "./base";

// Chưa có tạo

export const get_user_cart = async () => {
    const result = await get('/my_cart')
    if (result != null) {
        const data = await result.json();
        return data;
    } else {
        return {
            "products": [ //emptyable
              {
                "id": 0,
                "time_created": "string",
                "time_modified": "string",
                "price": 0,
                "infos": {
                  "additionalProp1": "string",
                  "additionalProp2": "string",
                  "additionalProp3": "string"
                },
                "name": "string",
                "ratings": []
              }
            ],
            "voucher": { // nullable
              "id": 0,
              "discount": 0,
              "received_time": "string",
              "expire_time": "string",
              "category_apply": "string",
              "description": "string"
            },
            "value": 0
          }
    }
}

export const get_user_orders = async () => {
    const result = await get('/my_orders')
    if (result != null) {
        const data = await result.json();
        return data;
    } else {
        return [
            {
              "id": 0,
              "items": [
                {
                  "product_id": 0,
                  "amount": 0
                }
              ],
              "status": "string",
              "time_created": "string",
              "time_completed": "string",
              "value": 0,
              "address": "string",
              "phone": "string",
              "user_id": 0
            }
        ]
    }
}

export const get_user_vouchers = async () => {
    const result = await get('/my_vouchers')
    if (result != null) {
        const data = await result.json();
        return data;
    } else {
        return [ // emptyable
            {
              "id": 0,
              "discount": 0,
              "received_time": "string",
              "expire_time": "string",
              "category_apply": "string",
              "description": "string"
            }
          ]
    }
}