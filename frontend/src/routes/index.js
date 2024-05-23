import LayoutDefault from "../Layout/LayoutDefault";
import Logout from "../pages/Logout";
import Home from "../pages/Home";
import Login from "../pages/Login";
import Register from "../pages/Register";
import Cart from "../components/Cart";
import ProductDetail from "../components/Product/User/ProductDetail";
import Checkout from "../pages/Checkout";
import Search from "../components/Search";
import PrivateRoute from "../components/PrivateRoute";
import LayoutAdmin from "../Layout/LayoutAdmin";
import Dashboard from "../pages/Dashboard";

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
                path: "/search",
                element: <Search />
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
                path: "/checkout",
                element: <Checkout />
            },
            {
                path: "*",
                element: <h1>404</h1>
            }
        ]
    },
    {
        element: <PrivateRoute />,
        children: [
            {
                element: <LayoutAdmin />,
                children: [
                    {
                        path: "/admin",
                        element: <Dashboard />
                    },
                ]
            }
        ]
    }
]