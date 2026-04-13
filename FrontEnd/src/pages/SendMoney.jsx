import { useState } from "react";
import api from "../services/api";

export default function SendMoney() {
  const [receiverId, setReceiverId] = useState("");
  const [amount, setAmount] = useState("");

  const sendMoney = async () => {
    try {
      await api.post("/remesa/send", null, {
        params: {
          sender_id: 1,
          receiver_id: receiverId,
          amount_usd: amount,
        },
      });

      alert("Remesa enviada");
    } catch (err) {
      console.log(err);
      alert("Error al enviar remesa");
    }
  };

  return (
    <div>
      <h2>Enviar dinero</h2>

      <input
        placeholder="Receiver ID"
        onChange={(e) => setReceiverId(e.target.value)}
      />

      <input
        placeholder="Amount USD"
        onChange={(e) => setAmount(e.target.value)}
      />

      <button onClick={sendMoney}>Enviar</button>
    </div>
  );
}