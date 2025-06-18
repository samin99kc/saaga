'use client';

import { Box, Typography, Button, Link, Container } from '@mui/material';
import Image from 'next/image';

export default function WelcomeSection() {
  return (
    <Container maxWidth="lg" sx={{ mt: 8 }}>
      <Box display="flex" flexDirection={{ xs: 'column', md: 'row' }} alignItems="center">
        {/* Text Section */}
        <Box flex={1} pr={{ md: 6 }} mb={{ xs: 4, md: 0 }} color={"black"}>
          <Typography variant="h4" fontWeight="bold" gutterBottom>
            Hi, I’m Jodi. Welcome to Legal Nomads.
          </Typography>

          <Typography paragraph>
            In 2008, I quit my job as a lawyer to visit Siberia. I started Legal Nomads to share photos and stories 
            from my travels with friends and family. I planned to take only a year sabbatical to travel the world.
          </Typography>

          <Typography paragraph>
            I never returned to the law. Instead, this site became the backbone of a new career in the decade that followed. 
            As its audience grew, so did my appetite. Food was the best way I could connect to others in a new place. 
            As a celiac, learning about food helped me navigate with less anxiety and chance of illness.
          </Typography>

          <Typography paragraph>
            In 2017, a lumbar puncture derailed my life when it left me with a chronic spinal CSF leak, and disabled. 
            Though my travels ground to a halt as a result, Legal Nomads remains a place to share lessons from the road, 
            gluten free travel guides, and alternative careers for those wanting to leave the practice of law. 
            On{' '}
            <Link href="#" underline="hover" color="primary">
              my sister site
            </Link>
            , I share resources about coping with grief and chronic pain, and what I’ve learned from this journey with chronic illness.
          </Typography>

          <Typography paragraph>
            Through it all, Legal Nomads remains a place to connect with others through curiosity and discovery. 
            I hope you enjoy reading!
          </Typography>

          <Button variant="contained" color="primary">
            More About Me →
          </Button>
        </Box>

        {/* Image Section */}
        <Box flex={1} display="flex" justifyContent="center">
          <Image
            src="/4799eba1-52c3-4773-93bf-15845a578f30.png"
            alt="Jodi smiling"
            width={400}
            height={400}
            style={{ maxWidth: '100%', height: 'auto', borderRadius: '12px' }}
          />
        </Box>
      </Box>
    </Container>
  );
}
