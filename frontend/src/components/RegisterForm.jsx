import { useState } from "react";
import axios from "axios";

export default function RegisterForm() {
  const [form, setForm] = useState({ username: "", email: "", password: "" });
  const [message, setMessage] = useState("");

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await axios.post("/register", form);
      setMessage("Registration successful! Please log in.");
    } catch {
      setMessage("Registration failed.");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input placeholder="Username" value={form.username} onChange={e => setForm({ ...form, username: e.target.value })} />
      <input placeholder="Email" value={form.email} onChange={e => setForm({ ...form, email: e.target.value })} />
      <input type="password" placeholder="Password" value={form.password} onChange={e => setForm({ ...form, password: e.target.value })} />
      <button type="submit">Register</button>
      {message && <p>{message}</p>}
    </form>
  );
}
