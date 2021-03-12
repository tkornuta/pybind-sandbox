from setuptools import setup

from pybind11.setup_helpers import Pybind11Extension, build_ext


ext_modules = [
    Pybind11Extension("my_math.ext", ["src/my_math_ext.cpp"]),
]

setup(
    name="my_math",
    version=0.1,
    author="tkornuta",
    author_email="tkornuta@gmail.com",
    description="An exemplary project using pybind11",
    install_requires=["pybind11"],
    tests_require=["pytest", "pytest-runner"],
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
