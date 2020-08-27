import React from 'react';

import APIClient from './client.js';

class HomeComponent extends React.Component {
  state = {
    recipes: [],
  };

  async componentDidMount() {
    this.client = new APIClient();
    this.client
      .getRecipeByIngredient('chicken')
      .then((data) =>
        this.setState({ ...this.state, recipes: data['tacos']['results'] })
      );
  }
  //   data) => JSON.parse(data['tacos']['result'])
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
        {this.state.recipes.map((recipe) =>
          Object.keys(recipe).map((obj) => <td>{recipe[obj]}</td>)
        )}
        <thead>
          <tr>
            <th>Link</th>
            <th>Ingredients</th>
            <th>Thumbnail</th>
            <th>Title</th>
          </tr>
        </thead>
        <tbody>
          <tr></tr>
        </tbody>

        {/* <tr>
          {this.state.recipes.map((recipe) => {
            // const obj = this.destructureArray(recipe);
            <td>{recipe}</td>;
            // <td>{recipe.ingredients}</td>;
          })}
        </tr> */}
        {/* <ul>
          {this.state.recipes.map((recipe) =>
            Object.keys(recipe).map((obj) => <li>{recipe[obj]}</li>)
          )}
        </ul> */}
      </table>
    );
  }
}

export default HomeComponent;
