import { Outlet } from "react-router-dom";

import Sidebar from "../Sidebar/Sidebar";
import Header from "../Header/Header";

import PageContainer from "../../ui/PageContainer/PageContainer";

import "./AppShell.css";

function AppShell() {

    return (

        <div className="app-shell">

            <Sidebar />

            <div className="app-content">

                <Header />

                <main className="page-content">

                    <PageContainer>

                        <Outlet />

                    </PageContainer>

                </main>

            </div>

        </div>

    );

}

export default AppShell;