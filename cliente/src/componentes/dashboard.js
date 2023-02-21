import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';

const socket = io.connect('http://localhost:5000');

function Dashboard() {
  const [status, setStatus] = useState(null);

  useEffect(() => {
    // Función que se ejecuta cuando se recibe un mensaje de socket con los datos de estado
    const handleStatusUpdate = (data) => {
      setStatus(data);
      console.log(data);
    };

    // Conectar al servidor de socket.io
    socket.on('connect', () => {
      console.log('Connected to server');
    });

    // Escuchar mensajes de socket con los datos de estado actualizados
    socket.on('status_update', handleStatusUpdate);

    // Desconectar del servidor de socket.io cuando se desmonta el componente
    return () => {
      socket.disconnect();
      console.log('Disconnected from server');
    };
  }, []);

  return (
    <div>
      <h1>Status Dashboard</h1>
      {status ? (
        <table>
          <thead>
            <tr>
              <th>CPU</th>
              <th>RAM</th>
              <th>Hard Disk</th>
            </tr>
          </thead>
            <tbody>
                <tr>
                    <td>{status.cpu}</td>
                    <td>{status.ram}</td>
                    <td>{status.disk}</td>
                </tr>
            </tbody>
        </table>):<div></div>}
    </div>)};

export default Dashboard;