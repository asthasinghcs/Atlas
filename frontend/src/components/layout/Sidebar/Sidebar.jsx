import { NavLink } from "react-router-dom";

import navigation from "./navigation";

import "./Sidebar.css";

function Sidebar() {
    return (
        <aside className="sidebar">

            <div className="sidebar-brand">

                <h1>ATLAS</h1>

                <p>Intelligence OS</p>

            </div>

            <nav className="sidebar-nav">

                {navigation.map((group) => (
                    <div
                        key={group.section ?? "root"}
                        className="nav-group"
                    >

                        {group.section && (
                            <p className="nav-section">
                                {group.section}
                            </p>
                        )}

                        {group.items.map((item) => (
                            <NavLink
                                key={item.path}
                                to={item.path}
                                className={({ isActive }) =>
                                    isActive
                                        ? "nav-link active"
                                        : "nav-link"
                                }
                            >
                                {item.label}
                            </NavLink>
                        ))}

                    </div>
                ))}

            </nav>

            <div className="sidebar-footer">

                <NavLink
                    to="/settings"
                    className="nav-link"
                >
                    Settings
                </NavLink>

            </div>

        </aside>
    );
}

export default Sidebar;