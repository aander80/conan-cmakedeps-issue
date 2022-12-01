from conan import ConanFile
from conan.tools.layout import basic_layout
from conan.tools.files import copy

class HeaderGeneratorConanRecipe(ConanFile):
    name = "header_generator"
    version = "0.0"
    exports_sources = "header_generator.py", "cmake/*.cmake"
    requires = "arbitrary_dep/0.0"

    def layout(self):
        basic_layout(self)

    def package(self):
        copy(self, "header_generator.py", self.source_folder, self.package_folder)
        copy(self, "cmake/*.cmake", self.source_folder, self.package_folder)

    def package_info(self):
        self.cpp_info.set_property("cmake_build_modules", ["cmake/header_generator.cmake"])
        self.cpp_info.set_property("cmake_find_mode", "both")
        self.env_info.PYTHONPATH.append(self.package_folder)
