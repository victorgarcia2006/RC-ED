import axios from "./axios";

export const getSimulationData = async () => axios.get('/simulation-data/');

export const getExperimentData = async () => axios.get('/experiment-data/');

export const deleteExperimentData = async () => axios.delete('/experiment-data/');