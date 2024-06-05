import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import BooksPage from "./pages/BooksPage";
import HomePage from "./pages/HomePage";

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route exact path="/" component={HomePage} />
          <Route exact path="/books" component={BooksPage} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
