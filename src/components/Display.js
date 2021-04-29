import React from 'react';
import { Container , Table} from 'semantic-ui-react';

const DataTable=({data})=>{

    if (data.length>0){
        return (
            <Container>
                <Table celled>
                    <Table.Header>
                        <Table.Row>
                            <Table.HeaderCell>strategy</Table.HeaderCell>
                            <Table.HeaderCell>instrument</Table.HeaderCell>
                            <Table.HeaderCell>ts</Table.HeaderCell>
                        </Table.Row>
                    </Table.Header>
                    <Table.Body>
                        {
                            data.map((entry, index)=>{
                                return (
                                    <Table.Row key={index}>
                                        <Table.Cell>{entry.signalName}</Table.Cell>
                                        <Table.Cell>{entry.signalInstrument}</Table.Cell>
                                        <Table.Cell>{entry.signalTs}</Table.Cell>
                                    </Table.Row>
                                )
                            })
                        }
                    </Table.Body>
                </Table>
            </Container>
        )
    } 
    
    return (
        <div>Loading...</div>
    )
}

export default DataTable;