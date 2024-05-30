import { useState, useEffect } from "react";
import styled from "@emotion/styled";

import { Table, TableBody, TableCell, TableHead, TableRow } from "@mui/material";

import "./css/DataTable.css";


export default function DataTable({ dataHeaders, data }) {
	const [sortedData, setSortedData] = useState([]);
  const [sortedFieldIndex, setSortedFieldIndex] = useState(0);
  const [isDesc, setIcDesc] = useState(false);  

  const handleSort = (field) => {
    let fieldIndex = dataHeaders.indexOf(field);
		
    if (fieldIndex === sortedFieldIndex) {
      setIcDesc(!isDesc);
    } else {
      setSortedFieldIndex(fieldIndex);
      setIcDesc(false);
    }
  };

  const headerWithIcon = (header) => {
    let HeaderIndex = dataHeaders.indexOf(header);
    let icon = "";

    if (HeaderIndex === sortedFieldIndex) 
			if(isDesc)
				icon = " ▼"
			else
				icon = " ▲";

    return header + icon;
  };

  useEffect(() => {		
		// check data existence
		if (!data) return;
		if (data.length < 1) return;

		// enable data sorting
    let RawDataHeaders = Object.keys(data[0]);
    let sortData = sort_by_field(data, RawDataHeaders[sortedFieldIndex], isDesc);

		setSortedData(sortData);
  }, [data, sortedFieldIndex, isDesc]);

  return (
    <div className="table">
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            {dataHeaders.map((header, index) => (
              <TableCell
                key={index}
                sx={{
                  cursor: "pointer",
                  fontSize: "1.2em",
                  fonrWeight: "bold",
									userSelect: "none",
                }}
                onClick={() => handleSort(header)}
              >
                {headerWithIcon(header)}
              </TableCell>
            ))}
          </TableRow>
        </TableHead>
        <TableBody>
          {sortedData.length > 0 ?
						sortedData.map((row, index) => (
							<TableRow
								key={index}
								sx={{ "&:last-child td": { border: 0 } }}
							>
								{Object.keys(row).map((key, index) => (
									<TableCell key={index}>{row[key]}</TableCell>
								))}
							</TableRow>
          	))
						:
						<tr>
							<td colSpan={dataHeaders.length}>Записи не найдены</td>
						</tr>
					}
        </TableBody>
      </Table>
    </div>
  );
}

const TableWrapper = styled("div")({
  width: "100vw",
});
export { TableWrapper };

function sort_by_field(array, field, desc) {
  const sortedArray = [...array];

  sortedArray.sort((a, b) => {
    if (a[field] < b[field]) return desc ? 1 : -1;
    if (a[field] > b[field]) return desc ? -1 : 1;
    return 0;
  });
  return sortedArray;
}
