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
      const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:8000';
      const res = await axios.post(`${apiUrl}/recommend`, filters);
      setRecommendations(res.data);
    } catch (err) {
      setError('Failed to get recommendations. Please check your backend and input.');
    }
  };

  return (
    <div>
      <div style={{textAlign: 'center'}}>
        <button onClick={handleClick}>Get Material Recommendation</button>
      </div>
      {error && <p className="error">{error}</p>}
      {recommendations.length > 0 && (
        <div className="recommendations">
          <h3>Recommended Materials:</h3>
          <ul>
            {recommendations.map((mat, i) => (
              <li key={i}>
                <b>{mat.name}</b><br/>
                <span>Strength: {mat.strength} MPa | Cost: ${mat.cost}/kg | Sustainability: {mat.sustainability}/10</span>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default RecommendMaterial;
