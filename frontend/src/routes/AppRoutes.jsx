import { Routes, Route } from "react-router-dom";

import AppShell from "../components/layout/AppShell/AppShell";

import Dashboard from "../pages/Dashboard/Dashboard";

function AppRoutes() {
    return (
        <Routes>

            <Route element={<AppShell />}>

                <Route
                    path="/"
                    element={<Dashboard />}
                />

            </Route>

        </Routes>
    );
}

export default AppRoutes;