import axios from "axios";
import DataTable from "./DataTable";
import { useState, useEffect } from "react";

export default function EventsListTable() {
    const [data, setData] = useState([])
    const columns = ["EL_ID", "EL_NAME", "EL_START_DATE", "EL_END_DATE", "EL_GROUP_ID", "EL_STUDENT_ID", "EL_STAFF_ID"];
    useEffect(() =>
        {
            axios.get('/event_list')
            .then(res => {
                setData(res.data.events)
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

