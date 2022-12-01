# CMakeDeps issue

This repo shows the issue I am currently having with CMakeDeps and transitive `tool_requires`/`requires`.

The dependency chain is:

* `clib` has a `tool_requires` towards `header_generator`.
* `header_generator` has a `requires` towards `arbitrary_dep`.

To reproduce the error, run the following commands from the repo root:

``` sh
conan create arbitrary_dep
conan create header_generator
mkdir -p clib/build
pushd clib/build
conan install ..
conan build ..
popd
```

This will generate the following error:

```
  Could not find a package configuration file provided by "arbitrary_dep"
  with any of the following names:

    arbitrary_depConfig.cmake
    arbitrary_dep-config.cmake

  Add the installation prefix of "arbitrary_dep" to CMAKE_PREFIX_PATH or set
  "arbitrary_dep_DIR" to a directory containing one of the above files.  If
  "arbitrary_dep" provides a separate development package or SDK, be sure it
  has been installed.
```

I am not sure what to do here. The CMakeDeps generated files seem to expect a reference to arbitrary_dep but is not generating these files itself. In this example, I am not interested in a CMake reference to arbitrary_dep, only to header_generator.

I found this issue on Github: https://github.com/conan-io/conan/issues/9951, where this is supposedly solved by adding `force_host_context=True` to the `tool_requires` call. I am not sure if that is what we are after, however, since `header_generator` is used to actually build the `clib` package, not test it (hence I am hesitant to use `test_requires` which I guess `tool_requires(..., force_host_context=True)` will turn into in conan 2.0?).
