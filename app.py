import pathlib
import runpy

runpy.run_path(
    str(pathlib.Path(__file__).parent / "dashboard" / "app.py"),
    run_name="__main__",
)
