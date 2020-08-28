import axios from 'axios';

const BASE_URI = 'http://localhost:5000';

const client = axios.create({
  baseURL: BASE_URI,
  json: true,
});

class APIClient {
  getRecipeByIngredient(ingredients) {
    return this.perform('get', `/tacos?ingredients=${ingredients}`);
  }

  getRecipeByDiet(diet) {
    return this.perform('get', `/tacos?diet=${diet}`);
  }

  getAllTacos() {
    return this.perform('get', '/tacos');
  }

  async perform(method, resource, data) {
    return client({
      method,
      url: resource,
      data,
      headers: { 'Access-Control-Allow-Origin': '*' },
    }).then((resp) => {
      return resp.data ? resp.data : [];
    });
  }
}

export default APIClient;
