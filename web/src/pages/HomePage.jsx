import React from "react";
import { Link } from "react-router-dom";
import Button from "@mui/material/Button";

function HomePage() {
  const welcome = "Welcome to FPT Smart Cloud Biblio";

  return (
    <div>
      <h1>{welcome}</h1>

      <Button
        variant="contained"
        component={Link}
        to={`/books`}
        style={{ marginRight: "8px" }}
      >
        View All Books
      </Button>
    </div>
  );
}

export default HomePage;
