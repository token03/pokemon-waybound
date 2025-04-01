# script obtained from https://gist.github.com/lhearachel/6793eda34a27d5462213a9f330eacb0c
import json
import pathlib

# [this file] -> root
root = pathlib.Path(__file__).resolve().parent
build = root / "build"

# Some flags here are commented out, as they are not recognized by clang
c_flags = [
    "/usr/bin/arm-none-eabi-gcc",
    "-c",
    "-mthumb",
    # '-mthumb-interwork',
    "-O2",
    "-mabi=apcs-gnu",
    "-mtune=arm7tdmi",
    "-march=armv4t",
    # '-fno-toplevel-reorder',
    "-lc",
    "-lgcc",
    "-Wno-pointer-to-int-cast",
    "-std=gnu17",
    "-Werror",
    "-Wall",
    "-Wno-strict-aliasing",
    "-Wno-attribute-alias",
    "-Woverride-init",
    "-D__CLANGD__",
    "-DMODERN",
    f"-I{root}/gflib",
    f"-I{root}/include",
    f"-include{root}/include/gba/types.h",
    f"-include{root}/include/global.h",
]

c_commands = [
    {
        "directory": build,
        "arguments": c_flags
        + [
            "-o",
            file.with_suffix(".o"),
            file.resolve(),
        ],
        "file": file.resolve(),
    }
    for file in (root / "src").rglob("*.c")
]

with open(root / "compile_commands.json", "w") as fout:
    json.dump(c_commands, fout, default=str, indent=4)
