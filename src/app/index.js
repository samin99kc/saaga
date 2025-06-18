// pages/index.js
import * as React from 'react';
import { Button, Typography, Container } from '@mui/material';

export default function Home() {
  return (
    <Container maxWidth="sm">
      <Typography variant="h3" gutterBottom>
        Welcome to Next.js with Material UI!
      </Typography>
      <Button variant="contained" color="primary">
        Get Started
      </Button>
    </Container>
  );
}
