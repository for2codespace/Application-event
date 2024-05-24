import axios from "axios";
import DataTable from "./DataTable";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";

export default function StudentsTable() {
    const [data, setData] = useState([])
    const columns = ["SB_BOARD_ID", "SB_CALENDAR_ID", "SB_STUDENT_ID", "SB_POSITION_ID"];
    const navigate = useNavigate();
    useEffect(() =>
        {
            axios.get('/student_board')
            .then(res => {
                if (res.status === 401) {
                    toast.error("Необходимо авторизоваться");
                    navigate("/auth#redirect=/students");
                }
                setData(res.data.board)
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

