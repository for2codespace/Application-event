import axios from "axios";
import DataTable from "./DataTable";
import { useState, useEffect } from "react";

export default function StudentsTable() {
    const [data, setData] = useState([])
    const columns = ["S_ID", "S_FIRSTNAME", "S_SURNAME", "S_LASTNAME", "S_GROUP_ID", "S_STUDY_ID"];
    useEffect(() =>
        {
            axios.get('/student')
            .then(res => {
                console.log(res.data.students)
                setData(res.data.students)
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

