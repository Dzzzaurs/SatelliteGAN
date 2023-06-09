import React, { useState } from 'react';

const LandscapeSelect = () => {
  const [selectedType, setSelectedType] = useState('');

  const handleTypeChange = (event) => {
    setSelectedType(event.target.value);
  };

  return (
    <div>
      <select value={selectedType} onChange={handleTypeChange}>
        <option value="">Select Landscape Type</option>
        <option value="mountain">Mountain</option>
        <option value="beach">Beach</option>
        <option value="forest">Forest</option>
        <option value="desert">Desert</option>
      </select>
      {selectedType && <p>Selected Landscape Type: {selectedType}</p>}
    </div>
  );
};

export default LandscapeSelect;