import LayoutDefault from "../LayoutDefault";
import Logout from "../pages/Logout";
import Home from "../pages/Home";
import Login from "../pages/Login";
import Register from "../pages/Register";
import Cart from "../components/Cart";
import ProductDetail from "../components/Product/User/ProductDetail";

export const routes = [
    // Public
    {
        path: "/",
        element: <LayoutDefault />,
        children: [
            {
                path: "/",
                element: <Home />
            },
            {
                path: "/login",
                element: <Login />
            },
            {
                path: "/register",
                element: <Register />
            },
            {
                path: "/logout",
                element: <Logout />
            },
            {
                path: "/cart",
                element: <Cart />
            },
            {
                path: "/product/:id",
                element: <ProductDetail />
            },
            {
                path: "*",
                element: <h1>404</h1>
            }
        ]
    }
]