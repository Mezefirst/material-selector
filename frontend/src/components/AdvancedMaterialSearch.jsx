import React, { useState } from 'react';
import { TextField, Slider, Select, MenuItem, Checkbox, ListItemText, Button, InputLabel, FormControl, Box } from '@mui/material';
import axios from 'axios';

const materialTypes = ['Metal', 'Polymer', 'Ceramic', 'Composite', 'Wood'];
const colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black', 'White'];

export default function AdvancedMaterialSearch({ onResults }) {
  const [filters, setFilters] = useState({
    types: [],
    colors: [],
    minStrength: 0,
    maxStrength: 1000,
    minCost: 0,
    maxCost: 500,
    minSustainability: 0,
    maxSustainability: 10,
    search: ''
  });

  const handleSearch = async () => {
    // Build filter query dynamically
    const payload = {
      types: filters.types,
      colors: filters.colors,
      min_strength: filters.minStrength,
      max_strength: filters.maxStrength,
      min_cost: filters.minCost,
      max_cost: filters.maxCost,
      min_sustainability: filters.minSustainability,
      max_sustainability: filters.maxSustainability,
      search: filters.search
    };
    const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:8000';
    const res = await axios.post(`${apiUrl}/recommend`, payload);
    onResults(res.data);
  };

  return (
    <Box sx={{ p: 2, background: '#fff', borderRadius: 2, boxShadow: 2 }}>
      <FormControl fullWidth sx={{ mb: 2 }}>
        <InputLabel id="type-label">Material Type</InputLabel>
        <Select
          labelId="type-label"
          multiple
          value={filters.types}
          onChange={e => setFilters({ ...filters, types: e.target.value })}
          renderValue={selected => selected.join(', ')}
        >
          {materialTypes.map(type => (
            <MenuItem key={type} value={type}>
              <Checkbox checked={filters.types.indexOf(type) > -1} />
              <ListItemText primary={type} />
            </MenuItem>
          ))}
        </Select>
      </FormControl>
      <FormControl fullWidth sx={{ mb: 2 }}>
        <InputLabel id="color-label">Color</InputLabel>
        <Select
          labelId="color-label"
          multiple
          value={filters.colors}
          onChange={e => setFilters({ ...filters, colors: e.target.value })}
          renderValue={selected => selected.join(', ')}
        >
          {colors.map(color => (
            <MenuItem key={color} value={color}>
              <Checkbox checked={filters.colors.indexOf(color) > -1} />
              <ListItemText primary={color} />
            </MenuItem>
          ))}
        </Select>
      </FormControl>
      <Box sx={{ mb: 2 }}>
        <InputLabel>Strength (MPa)</InputLabel>
        <Slider
          value={[filters.minStrength, filters.maxStrength]}
          min={0}
          max={2000}
          onChange={(_, v) => setFilters({ ...filters, minStrength: v[0], maxStrength: v[1] })}
          valueLabelDisplay="auto"
        />
      </Box>
      <Box sx={{ mb: 2 }}>
        <InputLabel>Cost ($/kg)</InputLabel>
        <Slider
          value={[filters.minCost, filters.maxCost]}
          min={0}
          max={1000}
          onChange={(_, v) => setFilters({ ...filters, minCost: v[0], maxCost: v[1] })}
          valueLabelDisplay="auto"
        />
      </Box>
      <Box sx={{ mb: 2 }}>
        <InputLabel>Sustainability (1–10)</InputLabel>
        <Slider
          value={[filters.minSustainability, filters.maxSustainability]}
          min={0}
          max={10}
          step={1}
          onChange={(_, v) => setFilters({ ...filters, minSustainability: v[0], maxSustainability: v[1] })}
          valueLabelDisplay="auto"
        />
      </Box>
      <TextField
        fullWidth
        label="Keyword Search"
        value={filters.search}
        onChange={e => setFilters({ ...filters, search: e.target.value })}
        sx={{ mb: 2 }}
        placeholder="Enter name, properties, or description..."
      />
      <Button variant="contained" color="primary" onClick={handleSearch}>Search</Button>
    </Box>
  );
}
