"use client";
import * as React from "react";
import {
  AppBar,
  Box,
  Toolbar,
  Typography,
  Button,
  Menu,
  MenuItem,
} from "@mui/material";
import KeyboardArrowDownIcon from "@mui/icons-material/KeyboardArrowDown";

const navItems = [
  { label: "ABOUT", submenu: ["Our Story", "Team"] },
  { label: "TOPICS", submenu: ["Health", "Recipes", "Travel"] },
  { label: "NEWSLETTER" },
  { label: "GLUTEN FREE" },
  { label: "RESOURCES", submenu: ["Guides", "Tools"] },
  { label: "CONTACT" },
];

export default function NavigationMenu() {
  const [anchorEls, setAnchorEls] = React.useState({});

  const handleClick = (event, index) => {
    setAnchorEls((prev) => ({ ...prev, [index]: event.currentTarget }));
  };

  const handleClose = (index) => {
    setAnchorEls((prev) => ({ ...prev, [index]: null }));
  };

  return (
    <AppBar position="static" color="transparent" elevation={0}>
      <Toolbar sx={{ display: "flex", justifyContent: "center", gap: 2 }}>
        {navItems.map((item, index) => (
          <Box key={index}>
            <Button
              onClick={(e) => item.submenu && handleClick(e, index)}
              endIcon={item.submenu ? <KeyboardArrowDownIcon /> : null}
              sx={{
                position: "relative",
                fontWeight: "bold",
                color: "black",
                textTransform: "none",
                "&::after": {
                  content: '""',
                  position: "absolute",
                  width: 0,
                  height: "2px",
                  left: 0,
                  bottom: 0,
                  backgroundColor: "#00d084",
                  transition: "width 0.3s ease",
                },
                "&:hover::after": {
                  width: "100%",
                },
              }}
            >
              {item.label}
            </Button>
            {item.submenu && (
              <Menu
                anchorEl={anchorEls[index]}
                open={Boolean(anchorEls[index])}
                onClose={() => handleClose(index)}
              >
                {item.submenu.map((option, i) => (
                  <MenuItem key={i} onClick={() => handleClose(index)}>
                    {option}
                  </MenuItem>
                ))}
              </Menu>
            )}
          </Box>
        ))}
      </Toolbar>
    </AppBar>
  );
}
