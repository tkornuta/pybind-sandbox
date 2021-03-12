# https://docs.bazel.build/versions/master/be/c-cpp.html#cc_library
load("@rules_cc//cc:defs.bzl", "cc_library")

cc_library(
    name = "my_math_ext",
    srcs = ["my_math_ext.cpp"],
    hdrs = ["my_math_ext.hpp"],
    deps = ["@pybind11_repo//:pybind11"]
)
