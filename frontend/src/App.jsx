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
    <div className="container">
      <h1>Material Selector</h1>
      <p style={{textAlign: 'center', color: '#7f8c8d', marginBottom: '30px'}}>
        Find sustainable materials for your engineering projects
      </p>
      <RecommendMaterial input={sampleInput} />
    </div>
  );
}

export default App;
