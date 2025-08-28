import RecommendMaterial from './components/RecommendMaterial';

function App() {
  const sampleInput = {
    cost_per_kg: 2.5,
    tensile_strength: 300,
    // You can add more fields as needed
    // sustainability: 6,
    // etc.
  };

  return (
    <div>
      <h1>Material Selector</h1>
      <RecommendMaterial input={sampleInput} />
    </div>
  );
}

export default App;
