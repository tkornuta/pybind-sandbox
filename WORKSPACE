workspace(name = "pybind_sandbox")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "pybind11_repo",
    build_file = "@//deps:BUILD.pybind11",
    sha256 = "1859f121837f6c41b0c6223d617b85a63f2f72132bae3135a2aa290582d61520",
    strip_prefix = "pybind11-2.5.0",
    type = "zip",
    url = "https://github.com/pybind/pybind11/archive/v2.5.0.zip",
)