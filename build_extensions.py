"""Compile the encrypted CFM loader modules into platform-specific extensions."""
from setuptools import Extension, setup
from Cython.Build import cythonize

MODULES = (
    "main", "pages", "relay_vless", "speed_limit", "telegram_bot",
    "xhttp_siz10", "anytls_bridge",
)

extensions = [Extension(name, [f"{name}.py"]) for name in MODULES]

setup(
    name="cfm-runtime",
    ext_modules=cythonize(
        extensions,
        build_dir="build/cython",
        compiler_directives={
            "language_level": 3,
            "embedsignature": False,
            "emit_code_comments": False,
            "binding": False,
            "linetrace": False,
        },
        annotate=False,
        quiet=True,
    ),
)
