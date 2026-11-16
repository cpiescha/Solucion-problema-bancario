"""Execute notebook code cells without requiring Jupyter and embed text outputs."""

from __future__ import annotations

import io
import json
import os
import sys
import traceback
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "simulacion_bancaria_tres_cajas.ipynb"


def stream_output(name: str, text: str) -> dict:
    return {"name": name, "output_type": "stream", "text": text.splitlines(keepends=True)}


def main() -> None:
    os.environ.setdefault("MPLBACKEND", "Agg")
    os.chdir(ROOT)
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))

    module = ModuleType("executed_banking_notebook")
    module.__file__ = str(NOTEBOOK)
    sys.modules[module.__name__] = module
    namespace = module.__dict__
    execution_count = 0

    for cell in notebook["cells"]:
        if cell.get("cell_type") != "code":
            continue

        execution_count += 1
        stdout = io.StringIO()
        stderr = io.StringIO()
        cell["execution_count"] = execution_count
        cell["outputs"] = []
        source = "".join(cell.get("source", []))

        try:
            with redirect_stdout(stdout), redirect_stderr(stderr):
                exec(compile(source, str(NOTEBOOK), "exec"), namespace)
        except Exception as exc:
            if stdout.getvalue():
                cell["outputs"].append(stream_output("stdout", stdout.getvalue()))
            if stderr.getvalue():
                cell["outputs"].append(stream_output("stderr", stderr.getvalue()))
            cell["outputs"].append(
                {
                    "ename": type(exc).__name__,
                    "evalue": str(exc),
                    "output_type": "error",
                    "traceback": traceback.format_exc().splitlines(),
                }
            )
            NOTEBOOK.write_text(json.dumps(notebook, ensure_ascii=False, indent=1), encoding="utf-8")
            raise

        if stdout.getvalue():
            cell["outputs"].append(stream_output("stdout", stdout.getvalue()))
        if stderr.getvalue():
            cell["outputs"].append(stream_output("stderr", stderr.getvalue()))

    NOTEBOOK.write_text(json.dumps(notebook, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Executed {execution_count} code cells in {NOTEBOOK.name}")


if __name__ == "__main__":
    main()
