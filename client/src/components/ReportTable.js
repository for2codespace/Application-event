import axios from "axios";
import DataTable from "./DataTable";
import { useState } from "react";
import { Button, Typography } from "@mui/material";
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import styled from "@emotion/styled";
import dayjs from "dayjs";

export default function EventsListTable() {
    const [date1, setDate1] = useState();
    const [date2, setDate2] = useState();
    const [data, setData] = useState([])
    const columns = ["ET_ID", "ET_TYPE", "ET_CLASS", "ET_NAME", "ET_EVENT_DATE", "ET_LOCATION", "ET_CALENDAR_ID"];
    const load_data = async () => {
        if (!date1 || !date2) 
            return alert('Выберите даты начала и конца периода')

        const date1AsDate = dayjs(date1);
        const date2AsDate = dayjs(date2);
    
        const formattedDate1 = date1AsDate.format('YYYY-DD-MM');
        const formattedDate2 = date2AsDate.format('YYYY-DD-MM');

        axios.get(`/event_type?date_from=${formattedDate1}&date_to=${formattedDate2}`)
        .then(res => {
            setData(res.data.event_types)
        })
        .catch(err => {
            setData(null)
        })
    }
    return (
        <div>
            <center><Typography variant="h4" sx={{ marginTop: '20px'}}>Отчет по событиям</Typography></center>
            <FormBox>
                <Typography variant="h5">Выберите даты начала и конца периода</Typography>
                <DatePicker onChange={(e) => setDate1(e)} />
                <DatePicker onChange={(e) => setDate2(e)} />
                <Button variant="contained" onClick={() => load_data()}>Показать</Button>
            </FormBox>
            { 
                data ?
                <DataTable dataHeaders={columns} data={data} />
                :
                <p>Записи не найдены</p>
            }
        </div>
    )
}

const FormBox = styled('div') ({
    display: 'grid',
    gridTemplateColumns: 'auto',
    width: '500px',
    '& > *': {
        margin: '10px'
    }
})