import { BrowserRouter, Routes, Route, redirect } from "react-router-dom";
import { LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { useState, createContext } from "react";
import { toast } from "react-toastify";

import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

import axios from "axios";
import Header from "./components/Header";
import GroupsTable from "./components/GroupsTable";
import StudentsTable from "./components/StudentsTable";
import EventCardsListPage from "./pages/EventCardsListPage";
import EventCardPage from "./pages/EventCardPage";
import AuthPage from "./pages/AuthPage";
import StaffTable from "./components/StaffTable";
import EventsListTable from "./components/EventsListTable";
import EventsLogTable from "./components/EventsLogTable";
import ReportTable from "./components/ReportTable";
import Redirect from "./components/Redirect";
import EventCardForm from "./components/EventCardForm";

const context = createContext();

export default function App() {
  const [auth, setAuth] = useState(localStorage.getItem("auth") === "true");
  const [user, setUser] = useState({
    name: localStorage.getItem("firstname"),
    lastname: localStorage.getItem("lastname"),
  });
  const set_auth = (value, firstname = null, lastname = null) => {
    setAuth(value);
    localStorage.setItem("auth", value);
    localStorage.setItem("firstname", firstname);
    localStorage.setItem("lastname", lastname);

    if (value === true) {
      setUser({ name: firstname, lastname: lastname });
    }
  };

  axios.defaults.baseURL = "https://cuddly-engine-pjjr6vqw5wpw267g7-5000.app.github.dev/api/";
  axios.defaults.headers.post["Content-Type"] = "application/json";
  axios.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error.response && error.response.status === 401) {
        toast.error("Необходимо авторизоваться");
        setAuth(false);
        let path = window.location.path;
        redirect("/auth#redirect=" + path);
      }
      return Promise.reject(error);
    },
  );

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <context.Provider value={{ auth, set_auth }}>
        <BrowserRouter>
          {auth === true ? (
            <>
              <Header user={user} />
              <Routes>
                <Route path="/" element={<Redirect url="/groups" />} />
                <Route path="/groups" element={<GroupsTable />} />
                <Route path="/students" element={<StudentsTable />} />
                <Route
                  path="/event-card-list"
                  element={<EventCardsListPage />}
                />
                <Route path="/event-card/:id" element={<EventCardPage />} />
                <Route path="/event-card-new" element={<EventCardForm />} />
                <Route path="/staff" element={<StaffTable />} />
                <Route path="/events-list" element={<EventsListTable />} />
                <Route path="/events-log" element={<EventsLogTable />} />
                <Route path="/report" element={<ReportTable />} />
                <Route path="/auth" element={<AuthPage />} />
              </Routes>
            </>
          ) : (
            <AuthPage />
          )}
        </BrowserRouter>
      </context.Provider>

      {/* toastify container for notifications */}
      <ToastContainer
        position="bottom-right"
        autoClose={5000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
        theme="colored"
      />
    </LocalizationProvider>
  );
}
export { context };
