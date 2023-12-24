import axios from "axios";
import DataTable from "./DataTable";
import { useState, useEffect } from "react";

export default function TableView({ endpoint_url }) {
    const [data, setData] = useState([])
    const [hasResponse, setHasResponse] = useState(false);
    useEffect(() =>
        {
            axios.get(endpoint_url)
            .then(res => { 
                setData(res.data.events);
                setHasResponse(true);
            })
            .catch(err => {
                setData(null);
                setHasResponse(true);
            })
        }, [])
    return (
        <div>
            { !hasResponse ? 
                (<div className="loader" />)
                 :                
                ( data ? 
                    (<DataTable data={data} />)
                     : 
                    (<p>Записи не найдены</p>)
                )
            }
        </div>
    )
}
