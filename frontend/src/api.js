import axios from 'axios';
import { ACCESS_TOKEN } from './constants';

const public_api = axios.create({
  baseURL: import.meta.env.VITE_API_URL
});

const auth_api = axios.create({
  baseURL: import.meta.env.VITE_API_URL
});

auth_api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export { public_api, auth_api };
