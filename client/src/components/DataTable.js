import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import './css/DataTable.css';
import styled from '@emotion/styled';

export default function DataTable({ dataHeaders, data }) {
    return (
        <div className='table'>
            <Table sx={{ minWidth: 650, maxWidth: '90vw' }} aria-label="simple table">
                <TableHead>
                    <TableRow>
                        {dataHeaders.map(
                            (header, index) => <TableCell key={index}>{header}</TableCell>
                        )}                                
                    </TableRow>
                </TableHead>
                <TableBody>
                    {data.map((row, index) => (
                        <TableRow
                            key={index}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                        >
                            { Object.keys(row).map((key, index) => 
                                <TableCell key={index}>{row[key]}</TableCell>)
                            }
                            { Object.keys(row).map((key, index) => console.log(row[key]))
                            }
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </div>
    );
}

const TableWrapper = styled('div') ({
    width: '100vw'
})
export {TableWrapper};
