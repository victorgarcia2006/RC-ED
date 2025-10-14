import React, { useEffect } from "react";
import { getSimulationData, deleteExperimentData } from "./api/monitoreo";
import ExperimentChart from "@/components/ExperimentChart";

function HomePage() {
  useEffect(() => {
    getSimulationData()
      .then((response) => console.log(response))
      .catch((error) => console.error(error));
  }, []);

  const handleDeleteExperimentData = () => {
    deleteExperimentData()
      .then((response) => console.log(response))
      .catch((error) => console.error(error));
  };

  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-gray-50 p-8">
      <ExperimentChart />
      <button
        className="bg-blue-700 hover:bg-blue-600 text-white p-2 rounded-md font-bold"
        onClick={() => handleDeleteExperimentData()}
      >
        Eliminar datos
      </button>
    </main>
  );
}

export default HomePage;
