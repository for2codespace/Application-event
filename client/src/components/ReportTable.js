import axios from "axios";
import DataTable from "./DataTable";
import { useState } from "react";
import { Button, Typography } from "@mui/material";
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { toast } from 'react-toastify';
import { useNavigate } from "react-router-dom";
import styled from "@emotion/styled";
import dayjs from "dayjs";

export default function EventsListTable() {
    const navigate = useNavigate();
    const [date1, setDate1] = useState();
    const [date2, setDate2] = useState();
    const [hasData, setHasData] = useState(false);
    const [data, setData] = useState([]);
    const columns = ["№", "Название", "Запланировано? (да/нет)", "место проведения", "наличие фото", "внутренняя ссылка", "внешняя ссылка", "студенты", "вид события", "тип события", "комментариии", "преподаватель", "даты начала и конца"];
    const load_data = async () => {
        if (!date1 || !date2) 
            return alert('Выберите даты начала и конца периода')

        const date1AsDate = dayjs(date1);
        const date2AsDate = dayjs(date2);
    
        const formattedDate1 = date1AsDate.format('YYYY-MM-DD');
        const formattedDate2 = date2AsDate.format('YYYY-MM-DD');

        axios.get(`/event_cards?date_from=${formattedDate1}&date_to=${formattedDate2}`)
        .then(res => {
            if (res.status === 400)
                toast.error("Введены неверные данные")

            if (res.status === 200) {
                setData(res.data.event_cards);
                setHasData(true);
                toast.success("Данные загружены");
            }
        })
        .catch(err => {
            if (err.response.status === 404)
                toast.error("Не найдено событий на указанном промежутке");
            else {
                console.log(err);
                toast.error("Произошла ошибка при загрузке данных. Попробуйте позже.");
            }
            setData([]);
            setHasData(true);
        })
    }
    return (
        <div>
            <center>
                <Typography variant="h4" sx={{ marginTop: '50px'}}>Отчет по событиям</Typography>
                <FormBox>
                    <Typography variant="h5" sx={{ marginTop: '20px'}}>Выберите даты начала и конца периода</Typography>
                    <DatePicker onChange={(e) => setDate1(e)} />
                    <DatePicker onChange={(e) => setDate2(e)} />
                    <Button variant="contained" onClick={() => load_data()}>Показать</Button>
                </FormBox>
                <br />
            </center>
            { 
                data.length > 0 ?
                <DataTable dataHeaders={columns} data={data} />
                :
                (hasData && <p>Записи не найдены</p>)
            }
        </div>
    )
}

const FormBox = styled('div') ({
    display: 'grid',
    gridTemplateColumns: 'auto',
    rowGap: '20px',
    width: '500px',
    '& > *': {
        margin: '10px'
    }
})