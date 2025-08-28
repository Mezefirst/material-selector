import axios from 'axios';
import { useState } from 'react';

function RecommendMaterial({ input }) {
  const [recommendations, setRecommendations] = useState([]);
  const [error, setError] = useState(null);

  const handleClick = async () => {
    setError(null);
    setRecommendations([]);
    try {
      // Map input to backend filter keys
      const filters = {
        max_cost: input.cost_per_kg,
        min_strength: input.tensile_strength,
        // You can add other mappings as needed
        // e.g., min_sustainability: input.sustainability
      };
      const res = await axios.post('http://localhost:8000/recommend', filters); // port 8000 for FastAPI
      setRecommendations(res.data);
    } catch (err) {
      setError('Failed to get recommendations. Please check your backend and input.');
    }
  };

  return (
    <div>
      <button onClick={handleClick}>Get Recommendation</button>
      {error && <p style={{color: 'red'}}>{error}</p>}
      {recommendations.length > 0 && (
        <ul>
          {recommendations.map((mat, i) => (
            <li key={i}>
              <b>{mat.name}</b> (Strength: {mat.strength}, Cost: {mat.cost}, Sustainability: {mat.sustainability})
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default RecommendMaterial;
