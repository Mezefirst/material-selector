import axios from 'axios';

function RecommendMaterial({ input }) {
  const handleClick = async () => {
    const res = await axios.post('/recommend', input);
    alert(`Recommended: ${res.data.recommended_material}`);
  };

  return <button onClick={handleClick}>Get Recommendation</button>;
}

export default RecommendMaterial;
