import axios from "axios";
import DataTable from "./DataTable";
import { useState, useEffect } from "react";

export default function StudentsTable() {
    const [data, setData] = useState([])
    const columns = ["SL_ID", "SL_FIRSTNAME", "SL_SURNAME", "SL_LASTNAME", "SL_DIVISION_ID", "SL_IS_WORKS"];
    useEffect(() =>
        {
            axios.get('/teachers')
            .then(res => {
                setData(res.data.staff)
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

