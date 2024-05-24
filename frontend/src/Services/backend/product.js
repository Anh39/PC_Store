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
export const getProductList = async (id) => {
    const result = await get(`product`)
    if (result != null) {
        const data = await result.json();
        for(let i=0;i<data.length;i++) {
            try {
                data[i]['thumbnail'] = data[i]['image_0']
            } catch {
                console.log(i)
            }
        }
        return data;
    } else {
        return []
    }
}
export const getProductDetail = async (id) => { 
    const result = await get(`product/?id=${id}`)
    if (result != null) {
        let data = await result.json();
        data = data[0];
        let images = []
        let i = 0
        while(true){
            let image = data[`image_${i}`]
            if (image == null) {
                break;
            } else {
                images.push(image);
                delete data[`image_${i}`]
            }
            i++
        }
        let basic_infos = []
        i = 0
        while(true){
            let basic_info = data[`basic_info_${i}`]
            if (basic_info == null) {
                break;
            } else {
                basic_infos.push(basic_info);
                delete data[`basic_info_${i}`]
            }
            i++
        }
        let detail_infos = []
        i = 0
        while(true){
            let detail_info = data[`detail_info_${i}`]
            if (detail_info == null) {
                break;
            } else {
                detail_infos.push(detail_info);
                delete data[`detail_info_${i}`]
            }
            i++
        }
        let notices = []
        i = 0
        while(true){
            let notice = data[`notice_${i}`]
            if (notice == null) {
                break;
            } else {
                notices.push(notice);
                delete data[`notice_${i}`]
            }
            i++
        }
        data['images'] = images
        data['basic_infos'] = basic_infos
        data['detail_infos'] = detail_infos
        data['notices'] = notices
        console.log(data)
        return data;
    } else {
        return null
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

export const getCategoryList = async () => {
    // const result = await get("category");
    const result = await get('product/category');
    if (result != null) {
        let data = await result.json();
        return data;
    } else {
        return []
    }
}