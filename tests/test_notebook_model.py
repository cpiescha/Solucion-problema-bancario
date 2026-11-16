"""Behavior tests for the executable model embedded in the notebook."""

from __future__ import annotations

import json
import os
import sys
import unittest
from pathlib import Path
from types import ModuleType

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "simulacion_bancaria_tres_cajas.ipynb"


def load_model_namespace() -> dict:
    """Execute only notebook cells tagged as ``model``."""
    os.environ.setdefault("MPLBACKEND", "Agg")
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    module = ModuleType("notebook_model_test")
    module.__file__ = str(NOTEBOOK)
    sys.modules[module.__name__] = module
    namespace = module.__dict__
    for cell in notebook["cells"]:
        tags = cell.get("metadata", {}).get("tags", [])
        if cell.get("cell_type") == "code" and "model" in tags:
            source = "".join(cell.get("source", []))
            exec(compile(source, str(NOTEBOOK), "exec"), namespace)
    return namespace


class NotebookModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ns = load_model_namespace()

    def test_activity_parameters_are_valid(self) -> None:
        self.ns["validar_parametros"](self.ns["PARAMETROS"])
        self.assertGreaterEqual(self.ns["N_REPLICAS"], 10)
        self.assertAlmostEqual(self.ns["PROB_ACCION"]["retiro"], 0.70)
        self.assertAlmostEqual(self.ns["PROB_ACCION"]["pago"], 0.30)

    def test_replica_is_reproducible_and_conserves_customers(self) -> None:
        simular = self.ns["simular_replica"]
        first, first_tellers = simular("tres_mixtas", semilla=2025)
        second, second_tellers = simular("tres_mixtas", semilla=2025)

        pd.testing.assert_frame_equal(first, second)
        pd.testing.assert_frame_equal(first_tellers, second_tellers)
        self.assertGreater(len(first), 0)
        self.assertEqual(len(first), int(first_tellers["usuarios_atendidos"].sum()))
        self.assertTrue((first["espera"] >= 0).all())
        self.assertTrue((first["fin_servicio"] >= first["inicio_servicio"]).all())
        self.assertTrue((first["inicio_servicio"] >= first["llegada"]).all())

    def test_exclusive_scenario_routes_each_action_to_eligible_teller(self) -> None:
        clientes, _ = self.ns["simular_replica"]("una_retiros_dos_pagos", semilla=17)
        roles = self.ns["ESCENARIOS"]["una_retiros_dos_pagos"]
        for row in clientes.itertuples(index=False):
            self.assertIn(row.accion, roles[row.cajero])

    def test_notebook_is_fully_executed_without_cell_errors(self) -> None:
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
        self.assertTrue(all(cell["execution_count"] is not None for cell in code_cells))
        self.assertFalse(
            any(
                output.get("output_type") == "error"
                for cell in code_cells
                for output in cell.get("outputs", [])
            )
        )
        stdout = "".join(
            "".join(output.get("text", []))
            for cell in code_cells
            for output in cell.get("outputs", [])
            if output.get("output_type") == "stream"
        )
        self.assertIn("Todas las validaciones finalizaron correctamente.", stdout)
        self.assertIn("CONCLUSIONES", stdout)
        self.assertTrue((ROOT / "resultados" / "comparacion_escenarios.png").exists())


if __name__ == "__main__":
    unittest.main()
