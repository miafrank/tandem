import React, { useState, useEffect } from 'react';

import APIClient from './client.js';

const HomeComponent = (props) => {
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    setRecipes(props.data);
    // const client = new APIClient();
    // client.getRecipeByIngredient(props.data).then((data) => {
    //   setRecipes(data['tacos']['results']);
    // });
  });
  console.log(props.data);
  const getKeys = function () {
    return recipes.map((recipe) => Object.keys(recipe));
  };

  const getValues = function () {
    return recipes.map((recipe) => Object.values(recipe));
  };

  const getHeader = function () {
    const keys = getKeys();
    return keys.map((k, i) => {
      return <th key={k[i]}>{k[i]}</th>;
    });
  };

  const getRowsData = function () {
    const data = getValues();
    const keys = getKeys();
    return data.map((k, i) => {
      return (
        <tr key={i}>
          <RenderRow key={i} data={k} keys={keys} />
        </tr>
      );
    });
  };
  return (
    <table>
      <thead>
        <tr>{getHeader()}</tr>
      </thead>
      <tbody>
        <tr>{getRowsData()}</tr>
      </tbody>
    </table>
  );
};

const RenderRow = (props) => {
  return props.keys.map((key, index) => {
    return <td key={props.data[key]}>{props.data[key]}</td>;
  });
};
export default HomeComponent;
