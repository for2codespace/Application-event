import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { LocalizationProvider } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs'
import axios from 'axios';
import Header from './components/Header';
import ReportPage from './pages/ReportPage';
import Redirect from './components/Redirect';
import TableView from './components/TableView';


export default function App() {
  axios.defaults.baseURL = 'https://application-event.onrender.com/api/';  // backend on render.com
  axios.defaults.headers.post['Content-Type'] = 'application/json';
  const TABLE_VIEW_ENDPOINTS = {
    "groups": "/groups",
    "students": "/student",
    "student-council": "/student_board",
    "staff": "/staff_list",
    "events-list": "/event_list",
    "events-log": "/event_type",
  }
  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <BrowserRouter>
        <Header />
        <Routes>

        {
          Object.entries(TABLE_VIEW_ENDPOINTS).map(([key, value]) => {
            return <Route key={key} path={`/${key}`} element={<TableView endpoint_url={value} />} />
          })
        }
          <Route path="/" element={<Redirect url="/groups" />} />
          <Route path="/report" element={<ReportPage />} />

        </Routes>
      </BrowserRouter>
    </LocalizationProvider>
  );
}
