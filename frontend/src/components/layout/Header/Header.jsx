import { useLocation } from "react-router-dom";

import routeConfig from "../../../routes/routeConfig";

import "./Header.css";

function Header() {

    const location = useLocation();

    const currentRoute =
        routeConfig.find(
            (route) => route.path === location.pathname
        ) || {
            title: "Atlas",
            subtitle: "Intelligence Operating System"
        };

    return (

        <header className="header">

            <div className="header-left">

                <h1 className="header-title">
                    {currentRoute.title}
                </h1>

                <p className="header-subtitle">
                    {currentRoute.subtitle}
                </p>

            </div>

            <div className="header-right">

                <button className="search-trigger">

                    Search Atlas

                </button>

                <div className="status-indicator">

                    <span className="status-dot"></span>

                    Live

                </div>

            </div>

        </header>

    );

}

export default Header;