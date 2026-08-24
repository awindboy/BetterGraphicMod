"""Validate dimensions and filename coverage for the full v159.7 sprite batch."""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sprites-override"
BUILDER = ROOT / "tools" / "build_full_vanilla_structure_resprites.py"


def load_builder():
    spec = importlib.util.spec_from_file_location("full_builder", BUILDER)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load full sprite builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--blocks-java", type=Path, required=True)
    parser.add_argument("--raw-sprites", type=Path, required=True)
    args = parser.parse_args()

    builder = load_builder()
    assets = builder.gather_assets(args.raw_sprites, builder.runtime_ids(args.blocks_java))
    errors: list[str] = []
    for source in assets:
        target = OUT / source.name
        if not target.exists():
            errors.append(f"missing: {source.name}")
            continue
        with Image.open(source) as raw_source, Image.open(target) as output:
            raw = raw_source.convert("RGBA")
            expected = (raw.width * builder.SCALE, raw.height * builder.SCALE)
            if output.size != expected:
                errors.append(f"wrong size: {source.name}: {output.size}, expected {expected}")
            if output.mode != "RGBA":
                errors.append(f"wrong mode: {source.name}: {output.mode}")
            if raw.getchannel("A").getbbox() and output.getchannel("A").getbbox() is None:
                errors.append(f"lost alpha content: {source.name}")

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated {len(assets)} Build 159.7 override regions: exact names, 8x dimensions, RGBA and non-empty alpha.")


if __name__ == "__main__":
    main()
