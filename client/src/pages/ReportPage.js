import { useState } from 'react';
import DataTable from '../components/DataTable';
import dayjs from "dayjs";

export default function ReportPage () {
    const [data, setData] = useState([]);
    const [formFilled, setFormFilled] = useState(false);
    const [params, setParams] = useState(null);

    const fetchData = () => {
        axios.get('/event_list', { params: params }).then(
            res => setData(res.data.events)
        ).catch(err => {
            alert("Прозошла неизвестная ошибка");
            console.log(err)
        })
    }
    const onSuccess = () => {
        setFormFilled(true);
        fetchData();
    }

    return (
        <>
            { formFilled ?
                (data ? <DataTable data={data} /> : <p>loading...</p>)
                :
                <Form setParams={setParams} onSuccess={onSuccess} />
            }
        </>
    );
}

function Form ({ setParams, onSuccess }) {
    const [date, setDate] = useState(null);

    const handleFormSubmit = () => {
        if (date) {
            setParams({ date: dayjs(date).format("YYYY-MM-DD") });
            onSuccess();
        }
    }

    return (
        <div className='form-wrapper'>
            <div className='form-title'>Отчет по событиям</div>
            <Typography variant="h5">Выберите даты начала и конца периода</Typography>
            <DatePicker onChange={(e) => setDate(e)} />
            <Button variant="contained" onClick={() => handleFormSubmit()}>Показать</Button>
        </div>
    )
}
