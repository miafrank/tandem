import React, { useState } from 'react';

import HomeComponent from './HomeComponent';
import APIClient from './client.js';

const SearchComponent = () => {
  const client = new APIClient();

  const [formData, setFormData] = useState({
    ingredients: '',
  });
  const onChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const { ingredients } = formData;

  const onSubmit = async (e) => {
    client
      .getRecipeByIngredient([ingredients])
      .then((data) => <HomeComponent data={data} />);
    // got data back here
  };

  return (
    <form className='form' onSubmit={(e) => onSubmit(e)}>
      <div className='form-group'>
        <input
          type='ingredients'
          placeholder='Search for ingredients'
          name='ingredients'
          value={ingredients}
          required
          onChange={(e) => onChange(e)}
        />
      </div>
      <input type='submit' className='btn btn-primary' value='find recipes!' />
    </form>
  );
};

export default SearchComponent;
