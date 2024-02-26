from spack.package import *

class Cufinufft(MakefilePackage, CudaPackage):
    """cufiNUFFT"""

    homepage = "https://github.com/AdhocMan/cufinufft.git"
    url = "https://github.com/AdhocMan/cufinufft/archive/refs/tags/v1.2-t3.tar.gz"
    git = "https://github.com/AdhocMan/cufinufft.git"

    version("1.2-t3", sha256="3e1872aad057510efaba7279ba8cc714fa8a4206bde92c8d3dc52c641e858098")

    conflicts("~cuda")
    conflicts("+cuda cuda_arch=none")

    patch("install_contrib.patch")

    def setup_build_environment(self, env):
        env.set("NVCC", self.spec["cuda"].prefix.bin.nvcc)
        env.set("CC", self.compiler.cc)
        env.set("CXX", self.compiler.cxx)

        cuda_archs = self.spec.variants["cuda_arch"].value
        cuda_arch_flags = " ".join(
            ["-gencode=arch=compute_{0},code=sm_{0}".format(x) for x in cuda_archs]
        )

        common_flags = "-O3 -fPIC"

        env.set("NVARCH", cuda_arch_flags)
        env.set("CFLAGS", common_flags)
        env.set("CXXFLAGS", "-std=c++14 {}".format(common_flags))
        env.set("NVCCFLAGS", "-std=c++14 -ccbin={0} {1} --default-stream per-thread -Xcompiler \"$(CXXFLAGS)\"".format(self.compiler.cxx, cuda_arch_flags))
        env.set("LIBS", "-Xlinker \"--disable-new-dtags\" -L{0} -Xlinker \"-rpath={0}\"".format(self.spec["cuda"].libs.directories[0]))


    @property
    def build_targets(self):
        spec = self.spec
        return ["lib"]

    def install(self, spec, prefix):
        install_tree("lib", prefix.lib)
        install_tree("include", prefix.include)
        #  mkdirp(join_path(prefix.include, "contrib"))
        #  install("contrib/*.h", join_path(prefix.include, "contrib"))

