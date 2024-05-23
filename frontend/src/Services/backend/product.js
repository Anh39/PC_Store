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

export const createProduct = async (option) => {
    const basic = [
        'time_created','time_modified','price','name','ratings'
    ]
    const infos = {}
    for (let key in option){
        if (!basic.includes(key)) {
            console.log(key);
            infos[key] = option[key];
        }
    }
    const data = {}
    for (let it in basic) {
        if (basic[it] in option) {
            data[basic[it]] = option[basic[it]];
        }
    }
    data['infos'] = {};
    for (let info in infos) {
        data['infos'][info] = infos[info];
    }
    if (data['ratings'] == null) {
        data['ratings'] = [];
    }
    const result = await post('product',data)
    if (result != null) {
       const id = await result.text()
       return id
    } else {
        return null
    }
}