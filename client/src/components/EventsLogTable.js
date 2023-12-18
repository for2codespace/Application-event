import axios from "axios";
import DataTable from "./DataTable";
import { useState, useEffect } from "react";

export default function EventsListTable() {
    const [data, setData] = useState([])
    const columns = ["ET_ID", "ET_TYPE", "ET_CLASS", "ET_NAME", "ET_EVENT_DATE", "ET_LOCATION", "ET_CALENDAR_ID"];
    useEffect(() =>
        {
            axios.get('/event_type')
            .then(res => {
                setData(res.data.event_types)
            })
            .catch(err => {
                setData(null)
            })
        }, [])
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

