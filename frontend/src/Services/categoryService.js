export const getCategoryList = async () => {
    // const result = await get("category");
    const response = await fetch("http://dummyjson.com/products/categories");
    const result = await response.json();
    return result;
}