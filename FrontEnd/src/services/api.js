import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");

  console.log("TOKEN EN REQUEST:", token); // 👈 IMPORTANTE

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  console.log("HEADERS:", config.headers); // 👈 VERIFICAR

  return config;
});

export default api;