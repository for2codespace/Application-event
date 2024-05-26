import axios from "axios";
import DataTable from "./DataTable";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function EventsListTable() {
    const [data, setData] = useState([])
    const columns = ["№", "Событие", "дата начала", "дата окончания", "группа", "студент", "преподаватель"];
    const navigate = useNavigate();
    
    useEffect(() =>
        {
            axios.get('/event_list')
            .then(res => {
                setData(res.data.events);
            })
            .catch(err => {
                setData(null);
            })
        }, [navigate])
    return (
        <div>
            { 
                data ?
                <DataTable dataHeaders={columns} data={data} />
                :
                <p>Записи не найдены</p>
            }
        </div>
    )
}

