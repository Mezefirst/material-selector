import RecommendMaterial from './components/RecommendMaterial';

function App() {
  const sampleInput = {
    cost_per_kg: 2.5,
    tensile_strength: 300,
    thermal_conductivity: 150,
    carbon_footprint: 5.0
  };

  return (
    <div>
      <h1>Material Selector</h1>
      <RecommendMaterial input={sampleInput} />
    </div>
  );
}

export default App;
