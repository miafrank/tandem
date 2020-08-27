import React from 'react';

import APIClient from './client.js';

class HomeComponent extends React.Component {
  constructor(props) {
    super(props);
    console.log(props);
    this.recipes = props.recipes;
  }
  state = {
    recipes: [],
  };

  async componentDidMount() {
    this.client = new APIClient();
    this.client.getRecipeByIngredient('chicken').then((data) => {
      this.setState({ ...this.state, recipes: data['tacos']['results'] });
    });
  }

  getKeys = function () {
    return this.state.recipes.map((recipe) => Object.keys(recipe));
  };

  getValues = function () {
    return this.state.recipes.map((recipe) => Object.values(recipe));
  };

  getHeader = function () {
    const keys = this.getKeys();
    return keys.map((k, i) => {
      return <th key={k[i]}>{k[i]}</th>;
    });
  };

  getRowsData = function () {
    const data = this.getValues();
    const keys = this.getKeys();

    return data.map((k, i) => {
      return (
        <tr key={i}>
          <RenderRow key={i} data={k} keys={keys} />
        </tr>
      );
    });
  };

  destructureArray(arr) {
    return {
      href: arr.href,
      ingredients: arr.ingredients,
      thumbnail: arr.thumbnail,
      title: arr.title,
    };
  }
  render() {
    return (
      <table>
        <thead>
          <tr>{this.getHeader()}</tr>
        </thead>
        <tbody>
          <tr>{this.getRowsData()}</tr>
        </tbody>
      </table>
    );
  }
}

const RenderRow = (props) => {
  return props.keys.map((key, index) => {
    return <td key={props.data[key]}>{props.data[key]}</td>;
  });
};
export default HomeComponent;
