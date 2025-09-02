import React from 'react';
import {
  Card, CardMedia, CardContent, Typography, IconButton, Toolbar, Box, Chip
} from '@mui/material';
import FavoriteIcon from '@mui/icons-material/Favorite';
import CompareIcon from '@mui/icons-material/Compare';
import BuildIcon from '@mui/icons-material/Build';
import AttachMoneyIcon from '@mui/icons-material/AttachMoney';

export default function MaterialCard({ material }) {
  const defaultImage = "https://images.unsplash.com/photo-1565049562-60c141c2f68a?w=400&h=200&fit=crop";
  
  return (
    <Card sx={{ maxWidth: 345, m: 1, height: '100%', display: 'flex', flexDirection: 'column' }}>
      <CardMedia
        component="img"
        height="140"
        image={material.image || defaultImage}
        alt={material.name}
        sx={{ objectFit: 'cover' }}
      />
      <CardContent sx={{ flexGrow: 1 }}>
        <Typography gutterBottom variant="h6" component="div">
          {material.name}
        </Typography>
        <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
          {material.properties || material.description}
        </Typography>
        
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
          {material.strength && (
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
              <BuildIcon color="action" fontSize="small" />
              <Typography variant="body2">
                Strength: {material.strength} MPa
              </Typography>
            </Box>
          )}
          
          {material.cost && (
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
              <AttachMoneyIcon color="action" fontSize="small" />
              <Typography variant="body2">
                Cost: ${material.cost}/kg
              </Typography>
            </Box>
          )}
          
          {material.sustainability && (
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
              <Typography variant="body2" sx={{ fontWeight: 'bold' }}>
                ♻️ Sustainability: {material.sustainability}/10
              </Typography>
            </Box>
          )}
        </Box>
        
        {material.type && (
          <Box sx={{ mt: 2 }}>
            <Chip label={material.type} size="small" color="primary" variant="outlined" />
          </Box>
        )}
      </CardContent>
      
      <Toolbar sx={{ justifyContent: 'space-between' }}>
        <IconButton color="primary" size="small">
          <FavoriteIcon />
        </IconButton>
        <IconButton color="secondary" size="small">
          <CompareIcon />
        </IconButton>
      </Toolbar>
    </Card>
  );
}