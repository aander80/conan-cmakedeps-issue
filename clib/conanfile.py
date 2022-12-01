from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain
from conan.tools.layout import cmake_layout
from conan.tools.files import copy

class CLibConanRecipe(ConanFile):
    name = "clib"
    version = "0.0"
    settings = "build_type"

    def layout(self):
        cmake_layout(self)

    def build_requirements(self):
        self.tool_requires("header_generator/0.0")
        # self.tool_requires("header_generator/0.0", force_host_context=True)
        self.tool_requires("cmake/3.25.0")
        self.tool_requires("ninja/1.11.0")
        self.tool_requires("mingw-builds/8.1")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generator = "Ninja"
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
