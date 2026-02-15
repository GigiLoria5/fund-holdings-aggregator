from pathlib import Path


def build_file_path_as_str(filename: str) -> str:
    return str(build_file_path(filename))


def build_file_path(filename: str) -> Path:
    return Path(__file__).parent / f"files/{filename}"
