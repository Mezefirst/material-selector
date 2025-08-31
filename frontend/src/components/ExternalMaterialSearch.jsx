import { useState } from "react";
import axios from "axios";

function ExternalMaterialSearch() {
  const [source, setSource] = useState("matweb");
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    const res = await axios.get(`/external-materials?source=${source}&query=${query}`);
    setResults(res.data);
  };

  return (
    <div>
      <select value={source} onChange={e => setSource(e.target.value)}>
        <option value="matweb">MatWeb</option>
        <option value="materials_project">Materials Project</option>
      </select>
      <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Search materials..." />
      <button onClick={handleSearch}>Search</button>
      <ul>
        {results.map((mat, idx) => <li key={idx}>{mat.name || mat.material_id}</li>)}
      </ul>
    </div>
  );
}

export default ExternalMaterialSearch;
