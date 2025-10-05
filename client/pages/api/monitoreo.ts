import axios from "./axios";

export const getSimulationData = async () => axios.get('/simulation-data/');