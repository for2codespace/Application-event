import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { LocalizationProvider } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs'
import axios from 'axios';
import Header from './components/Header';
import ReportPage from './pages/ReportTable';
import Redirect from './components/Redirect';
import TableView from './components/TableView';


export default function App() {
  axios.defaults.baseURL = 'https://application-event.onrender.com/api/';  // backend on render.com
  axios.defaults.headers.post['Content-Type'] = 'application/json';
  TABLE_VIEW_ENDPOINTS = {
    "groups": "/groups",
    "students": "/student",
    "student-council": "/student_board",
    "staff": "/staff_list",
    "events_list": "/events_list",
    "events_log": "/event_type",
  }
  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <BrowserRouter>
        <Header />
        <Routes>

          {
            Object.keys(TABLE_VIEW_ENDPOINTS).map((table) => 
              <Route 
                path={`/${table}`} 
                element={<TableView url={TABLE_VIEW_ENDPOINTS[table]} />} 
              />)
          }
          <Route path="/" element={<Redirect url="/groups" />} />
          <Route path="/report" element={<ReportPage />} />

        </Routes>
      </BrowserRouter>
    </LocalizationProvider>
  );
}
