import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8080',
});

const generateImage = (seed, landscapeType) => {
  return axiosInstance.get('/image', {
    params: {
      seed: seed,
      landscape: landscapeType,
    },
  });
};

export default generateImage;