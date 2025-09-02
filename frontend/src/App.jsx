import React, { useState } from 'react';
import {
  AppBar, Toolbar, Typography, IconButton, Container, Grid, Card, CardMedia,
  CardContent, Button, TextField
} from '@mui/material';
import FavoriteIcon from '@mui/icons-material/Favorite';
import CompareIcon from '@mui/icons-material/Compare';
import AdvancedMaterialSearch from './components/AdvancedMaterialSearch';
import MaterialCard from './components/MaterialCard';

const sampleMaterials = [
  {
    id: 1,
    name: "Acme Stainless Steel",
    image: "https://images.unsplash.com/photo-1519125323398-675f0ddb6308",
    properties: "Durable, Rust Resistant",
    strength: 500,
    cost: 2.0,
    sustainability: 5
  },
  {
    id: 2,
    name: "Eco Bamboo",
    image: "https://images.unsplash.com/photo-1465101046530-73398c7f28ca",
    properties: "Sustainable, Lightweight",
    strength: 100,
    cost: 1.0,
    sustainability: 10
  }
];

export default function App() {
  const [materials, setMaterials] = useState(sampleMaterials);

  return (
    <>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>Material Selector</Typography>
          <TextField size="small" placeholder="Search materials..." sx={{ mr: 2 }} />
          <IconButton color="inherit"><FavoriteIcon /></IconButton>
        </Toolbar>
      </AppBar>
      <Container>
        <Typography variant="h4" sx={{ mt: 4, mb: 4 }}>Smart Material Selection</Typography>
        <AdvancedMaterialSearch onResults={setMaterials} />
        
        <Typography variant="h5" sx={{ mt: 4, mb: 2 }}>
          {materials.length > 0 ? 'Recommended Materials' : 'Featured Materials'}
        </Typography>
        <Grid container spacing={2}>
          {materials.map(m => (
            <Grid item key={m.id} xs={12} md={6} lg={4}>
              <MaterialCard material={m} />
            </Grid>
          ))}
        </Grid>
        {materials.length === 0 && (
          <Button variant="contained" color="primary" sx={{ mt: 4 }}>Explore More</Button>
        )}
      </Container>
    </>
  );
}

