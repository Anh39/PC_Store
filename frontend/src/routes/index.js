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
import History from "../pages/History";
import HistoryAdmin from "../pages/HistoryAdmin";
import Success from "../pages/ReturnPayment/success";
import Failure from "../pages/ReturnPayment/failure";
import PC from "../pages/Category/pc";
import Laptop from "../pages/Category/laptop";
import Display from "../pages/Category/display";
import Auxility from "../pages/Category/auxility";

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
                path: "/search/:keyword",
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
            },
            {
                path: "/history",
                element: <History />
            },
            {
                path: "/success",
                element: <Success />
            },
            {
                path: "/failure",
                element: <Failure />
            },
            {
                path: "/pc",
                element: <PC />
            },
            {
                path: "/laptop",
                element: <Laptop />
            },
            {
                path: "/display",
                element: <Display />
            },
            {
                path: "/auxility",
                element: <Auxility />
            },
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
                    {
                        path: "/historyadmin",
                        element: <HistoryAdmin />
                    }
                ]
            }
        ]
    }
]