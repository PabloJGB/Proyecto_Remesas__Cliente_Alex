import { useEffect, useState } from "react";
import api from "../services/api";
import { LineChart, Line, XAxis, YAxis, Tooltip } from "recharts";
import { Link } from "react-router-dom";

export default function Dashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await api.get("/remesa");
        setData(res.data);
      } catch (err) {
        console.log(err);
        alert("Error cargando remesas");
      }
    };

    fetchData();
  }, []);
  
  return (
    <div>
      <h2>Historial de Remesas</h2>

      <LineChart width={600} height={300} data={data}>
        <XAxis dataKey="created_at" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="amount_usd" />
      </LineChart>
    </div>
  );

  <Link to="/send">
  <button>Enviar dinero</button>
</Link>
}