import APIClient from './client.js';

const client = new APIClient();
const call = client
  .getRecipeByIngredient('chicken')
  .then((data) => console.log(data['tacos']['']));
