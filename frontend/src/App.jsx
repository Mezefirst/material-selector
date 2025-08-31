import React from 'react';
import {
  AppBar, Toolbar, Typography, IconButton, Container, Grid, Card, CardMedia,
  CardContent, Button, TextField
} from '@mui/material';
import FavoriteIcon from '@mui/icons-material/Favorite';
import CompareIcon from '@mui/icons-material/Compare';

const materials = [
  {
    id: 1,
    name: "Acme Stainless Steel",
    image: "https://images.unsplash.com/photo-1519125323398-675f0ddb6308",
    properties: "Durable, Rust Resistant",
  },
  {
    id: 2,
    name: "Eco Bamboo",
    image: "https://images.unsplash.com/photo-1465101046530-73398c7f28ca",
    properties: "Sustainable, Lightweight",
  }
];

function MaterialCard({ material }) {
  return (
    <Card sx={{ maxWidth: 345, m: 2 }}>
      <CardMedia
        component="img"
        height="140"
        image={material.image}
        alt={material.name}
      />
      <CardContent>
        <Typography gutterBottom variant="h6" component="div">
          {material.name}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          {material.properties}
        </Typography>
      </CardContent>
      <Toolbar>
        <IconButton color="primary"><FavoriteIcon /></IconButton>
        <IconButton color="secondary"><CompareIcon /></IconButton>
      </Toolbar>
    </Card>
  );
}

function App() {
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
        <Typography variant="h4" sx={{ mt: 4 }}>Featured Materials</Typography>
        <Grid container spacing={2}>
          {materials.map(m => (
            <Grid item key={m.id} xs={12} md={6} lg={4}>
              <MaterialCard material={m} />
            </Grid>
          ))}
        </Grid>
        <Button variant="contained" color="primary" sx={{ mt: 4 }}>Explore More</Button>
      </Container>
    </>
  );
}

export default App;

