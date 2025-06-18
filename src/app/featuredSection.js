// FeaturedSection.jsx
"use client";
import { Box, Typography, Container } from "@mui/material";
import Image from "next/image";

export default function FeaturedSection() {
  return (
    <Box sx={{ bgcolor: "#fff", py: 6, color: "black" }}>
      <Container maxWidth="md">
        <Typography
          variant="h6"
          align="center"
          fontWeight="bold"
          gutterBottom
          sx={{ mb: 3 }}
        >
          FEATURED IN:
        </Typography>

        <Box
          display="flex"
          justifyContent="center"
          alignItems="center"
          flexWrap="wrap"
          gap={4}
          mb={5}
        >
          <Image
            src="/e64e0a42-a7c5-4a02-87cf-26f98152e151.png"
            alt="Featured Logos"
            width={800}
            height={100}
            style={{ maxWidth: "100%", height: "auto" }}
          />
        </Box>

        <Typography
          variant="h5"
          align="center"
          fontWeight="bold"
          sx={{ mt: 4 }}
        >
          WHAT ARE YOU CURIOUS ABOUT TODAY?
        </Typography>
      </Container>
    </Box>
  );
}
