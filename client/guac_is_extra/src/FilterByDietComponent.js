import React, { useState } from 'react';

import HomeComponent from './HomeComponent';
import APIClient from './client.js';

const client = new APIClient();

const FiltereByDietComponent = () => {
  const [selectedDiet, setSelectedDiet] = useState('');
  const diets = [
    'vegan',
    'vegetarian',
    'halal',
    'kosher',
    'gluten-free',
    'dairy-free',
    'nut allergy',
  ];

  const onChange = (e) => {
    setSelectedDiet(selectedDiet);
  };

  const onSubmit = async (e) => {
    const call = client
      .getRecipeByDiet(selectedDiet)
      .then((data) => console.log(data));
    // got data back here
  };

  return (
    <form className='form' onSubmit={(e) => onSubmit(e)}>
      <select
        value={selectedDiet}
        setSelectedDiet={selectedDiet}
        onChange={(e) => onSubmit(e)}
      >
        {diets.map((diet) => (
          <option value={diet} key={diet}>
            {diet}
          </option>
        ))}
      </select>
    </form>
  );
};

export default FiltereByDietComponent;
