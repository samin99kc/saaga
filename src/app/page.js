"use client";
import * as React from "react";
import NavigationMenu from "./navigation";
import { Box, Typography, Container } from "@mui/material";
import WelcomeSection from "./welcomeSection";
import FeaturedSection from "./featuredSection";

import Image from "next/image";

export default function Homepage() {
  return (
    <>
      <NavigationMenu />
      <Box sx={{ bgcolor: "#fff", py: 6 }}>
        <Container maxWidth="lg">
          <Box
            display="flex"
            flexDirection={{ xs: "column", md: "row" }}
            alignItems="center"
            justifyContent="center"
            textAlign={{ xs: "center", md: "left" }}
          >
            {/* Crow Image */}
            <Box
              flex={1}
              display="flex"
              justifyContent="center"
              mb={{ xs: 4, md: 0 }}
            >
              <Image
                src="/background.png"
                alt="Legal Nomads Crow Logo"
                width={600}
                height={300}
                style={{ maxWidth: "100%", height: "auto" }}
                priority
              />
            </Box>
          </Box>
        </Container>
      </Box>
      <WelcomeSection />
      <FeaturedSection/>
    </>
  );
}
