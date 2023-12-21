import axios from "axios";
import DataTable, { TableWrapper } from "./DataTable";
import { useState, useEffect } from "react";

export default function StaffTable() {
    const [data, setData] = useState([])
    const columns = ["SL_ID", "SL_FIRSTNAME", "SL_SURNAME", "SL_LASTNAME", "SL_DIVISION_ID", "SL_IS_WORKS"];
    useEffect(() =>
        {
            axios.get('/staff_list')
            .then(res => {
                setData(res.data.staff)
            })
            .catch(err => {
                setData(null)
            })
        }, [])
    return (
        <TableWrapper>
            { 
                data ?
                <DataTable dataHeaders={columns} data={data} />
                :
                <p>Записи не найдены {data.length}</p>
            }
        </TableWrapper>
    )
}

