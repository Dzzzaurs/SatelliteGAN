import React, { useState } from 'react';
import axios from 'axios';

const ImageGenerator = () => {
  const [seed, setSeed] = useState('');
  const [landscapeType, setLandscapeType] = useState('');
  const [generatedImage, setGeneratedImage] = useState('');

  const handleSeedChange = (event) => {
    setSeed(event.target.value);
  };

  const handleTypeChange = (event) => {
    setLandscapeType(event.target.value);
  };

  const handleGenerateImage = () => {
    axios
      .get('/generate-image', {
        params: {
          seed: seed,
          landscapeType: landscapeType,
        },
      })
      .then((response) => {
        setGeneratedImage(response.data.image);
      })
      .catch((error) => {
        console.error('Error generating image:', error);
      });
  };

  return (
    <div>
      <input
        type="text"
        value={seed}
        onChange={handleSeedChange}
        placeholder="Enter generation seed"
      />

      <select value={landscapeType} onChange={handleTypeChange}>
        <option value="">Select Landscape Type</option>
        <option value="mountain">Mountain</option>
        <option value="beach">Beach</option>
        <option value="forest">Forest</option>
        <option value="desert">Desert</option>
      </select>

      <button onClick={generateImage(seed, landscapeType)}>Generate Image</button>

      {generatedImage && (
        <img src={generatedImage} alt="Generated Satellite Image" />
      )}
    </div>
  );
};

export default ImageGenerator;