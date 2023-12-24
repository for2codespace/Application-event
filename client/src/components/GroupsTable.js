import axios from "axios";
import DataTable from "./DataTable";
import { useState, useEffect } from "react";

export default function StudentsTable() {
    const [data, setData] = useState([])
    const columns = ["GL_ID", "GL_NAME", "GL_YEAR"];
    useEffect(() =>
        {
            axios.get('/groups')
            .then(res => {
                setData(res.data.groups)
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

