const cartReducer = (state = [], action) => {
    let newState = [...state];

    switch (action.type) {
        case "ADD_TO_CART":
            return [...state, {
                id: action.id,
                amount: 1
            }];
        case "UPDATE_QUANTITY":
            const itemUpdate = newState.find(item => item.id === action.id);
            itemUpdate.amount = action.amount;
            return newState;
        case "DELETE_ITEM":
            newState = newState.filter(item => item.id !== action.id);
            return newState;
        case "DELETE_ALL":
            newState = [];
            return newState;
        default:
            return state;
    }
}

export default cartReducer;