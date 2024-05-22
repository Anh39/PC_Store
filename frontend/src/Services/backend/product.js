import { get,post} from "./base";

// Chưa có tạo

export const get_product = async (id) => {
    const result = await get(`/product?id=${id}`)
    if (result != null) {
        const data = await result.json();
        return data;
    } else {
        return [
            {
              "id": 10,
              "name": "string",
              "time_created": "2024-01-01 12:20:30",
              "time_modified": "2024-02-02 12:25:31",
              "price": 0,
              "ratings": [],
              "detail": "nothing here" // vô hạn trường dữ liệu
            }
          ]
    }
}

export const create_product = async (id) => {
    const option = {
        'time_created' : null,
        'time_modified' : null,
        'price' : 0,
        'infos' : {},
        'name' : null,
        'ratings' : []
    }
// Ví dụ cho option
// {
// "time_created": "2022-01-01 10:20:20",
// "time_modified": "2022-01-01 10:20:20",
// "price": 0,
// "infos": { // emptyalble
//     "additionalProp1": "string",
//     "additionalProp2": "string",
//     "additionalProp3": "string"
// },
// "name": "string",
// "ratings": []
// }
    const result = await post('product',option)
    if (result != null) {
       const id = await result.text()
       return id
    } else {
        return null
    }
}