import { del, get,patch,post} from "./base";

export const getProductList = async (id) => {
    const result = await get(`product?limit=100`)
    if (result != null) {
        const data = await result.json();
        // for(let i=0;i<data.length;i++) {
        //     try {
        //         data[i]['thumbnail'] = data[i]['image_0']
        //     } catch {
        //         console.log(i)
        //     }
        // }
        return data;
    } else {
        return []
    }
}
export const deleteProduct = async (id) => {
    const result = await del(`product?id=${id}`)
    if (result != null) {
        const data = await result.json();
        return data;
    } else {
        return []
    }
}
export const searchProductList = async (name) => {
    const result = await get(`product?name=${name}`)
    if (result != null) {
        const data = await result.json();
        // for(let i=0;i<data.length;i++) {
        //     try {
        //         data[i]['thumbnail'] = data[i]['image_0']
        //     } catch {
        //         console.log(i)
        //     }
        // }
        return data;
    } else {
        return []
    }
}
export const getProductDetail = async (id) => { 
    const result = await get(`product_detail?id=${id}`)
    if (result != null) {
        let data = await result.json();
        data = data[0];
        let basic_infos = []
        let i = 0
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
        data['images'].reverse()
        data['images'] = data['images'].slice(0,6)
        data['basic_infos'] = basic_infos
        data['detail_infos'] = detail_infos
        data['notices'] = notices
        return data;
    } else {
        return null
    }
}

export const getCategoryProduct = async (option) => {
    const result = await get(`product?category=${option}`)
    if (result != null) {
        const data = await result.json();
        return data;
    } else {
        return []
    }
}
export const createProduct = async (option) => {
    let data = option
    for (let i=0;i<option.basic_infos.length;i++) {
        option[`basic_info_${i}`] = option.basic_infos[i]
    }
    delete option.basic_infos
    for (let i=0;i<option.images.length;i++) {
        option.images[i] = {
            'path' : option.images[i],
            'order' : i
        }
    }
    data['thumbnail'] = data.images[0].path
    const result = await post('product',data)
    if (result != null) {
       const id = await result.text()
       return id
    } else {
        return null
    }
}

export const updateProduct = async (id,option) => {
    let data = option

    for (let i=0;i<option.images.length;i++) {
        option.images[i] = {
            'path' : option.images[i],
            'order' : i
        }
    }
    for (let i=0;i<option.basic_infos.length;i++) {
        option[`basic_info_${i}`] = option.basic_infos[i]
    }
    data['thumbnail'] = data.images[0].path
    data['name'] = 'abc'
    delete option.basic_infos

    const result = await patch(`product?id=${id}`,data)
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

export const getSearch = async (keyword) => {
    const result = await get(`product/?name=${keyword}`);
    if (result != null) {
        const data = await result.json();
        return data;
    } else {
        return [];
    }
}