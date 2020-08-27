import React from 'react';
import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';

import HomeComponent from './HomeComponent';
import SearchComponent from './SearchComponent';
import FilterByDietComponent from './FilterByDietComponent';

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to='/search'>Search By Ingredient</Link>
            </li>
            <li>
              <Link to='/filter'>Filter By Diet</Link>
            </li>
            <li>
              <Link to='/home'>Home</Link>
            </li>
          </ul>
        </nav>

        <Switch>
          <Route path='/search'>
            <SearchComponent />
          </Route>
          <Route path='/filter'>
            <FilterByDietComponent />
          </Route>
          <Route path='/home'>
            <HomeComponent />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
