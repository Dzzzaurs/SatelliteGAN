import React, { useState } from 'react';

const TextFieldWithSeed = () => {
  const [seed, setSeed] = useState('');

  const handleInputChange = (event) => {
    setSeed(event.target.value);
  };

  const handleGenerateClick = () => {
    // Perform generation logic with the provided seed
    // You can use the seed to generate satellite images or any other desired content
    // Example: generateImage(seed);

    // Clear the input field after generating
    setSeed('');
  };

  return (
    <div>
      <input
        type="text"
        value={seed}
        onChange={handleInputChange}
        placeholder="Enter generation seed"
      />
      <button onClick={handleGenerateClick}>Generate</button>
    </div>
  );
};

export default TextFieldWithSeed;