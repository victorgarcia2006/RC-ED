import { useEffect, useState } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";
import { getSimulationData, getExperimentData } from "@/pages/api/monitoreo";

interface DataPoint {
  t: number;
  v: number;
}

export default function ExperimentChart() {
  const [simulationData, setSimulationData] = useState<DataPoint[]>([]);
  const [experimentData, setExperimentData] = useState<DataPoint[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [expRes, simRes] = await Promise.all([
          getExperimentData(),
          getSimulationData(),
        ]);

        // Asignamos directamente los datos recibidos
        setExperimentData(expRes.data || []);
        setSimulationData(simRes.data || []);
      } catch (error) {
        console.error("Error al obtener datos:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="w-full h-[400px] flex items-center justify-center text-gray-600">
        Cargando datos...
      </div>
    );
  }

  // Fusionamos ambos conjuntos para que Recharts pueda usar un mismo gráfico
  // pero cada línea usará sus propias claves dataKey
  const allData = [
    ...experimentData.map((p) => ({ t: p.t, v_exp: p.v })),
    ...simulationData.map((p) => ({ t: p.t, v_sim: p.v })),
  ];

  console.log(allData)

  return (
    <div className="w-full h-[500px] bg-white p-4 rounded-2xl shadow-md">
      <h2 className="text-xl font-semibold mb-4 text-center">
        Comparación de voltaje vs tiempo
      </h2>
      <ResponsiveContainer width="100%" height="90%">
        <LineChart data={allData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis
            dataKey="t"
            label={{
              value: "Tiempo (s)",
              position: "insideBottom",
              offset: -5,
            }}
          />
          <YAxis
            domain={[0, "auto"]}
            label={{
              value: "Voltaje (V)",
              angle: -90,
              position: "insideLeft",
            }}
          />
          <Tooltip />
          <Legend />

          {/* Línea experimental */}
          <Line
            type="monotone"
            dataKey="v_exp"
            data={allData}
            stroke="#2563eb"
            strokeWidth={2}
            dot={true}
            name="Experimental"
          />

          {/* Línea simulación */}
          <Line
            type="monotone"
            dataKey="v_sim"
            data={allData}
            stroke="#16a34a"
            strokeWidth={2}
            dot={true}
            name="Simulación"
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}