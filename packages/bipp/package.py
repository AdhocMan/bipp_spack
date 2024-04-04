from spack.package import *

class Bipp(CMakePackage, CudaPackage):
    """bipp"""

    homepage = "https://github.com/epfl-radio-astro/bipp"
    url = "https://github.com/epfl-radio-astro/bipp"
    git = "https://github.com/epfl-radio-astro/bipp.git"

    version("main", branch="main")

    variant("openmp", default=True, description="Build with OpenMP support")
    variant("python", default=True, description="Build python module")
    variant("mpi", default=False, description="Build with MPI support")

    depends_on("blas")
    depends_on("lapack")
    depends_on("finufft@2.1.0")
    depends_on("spdlog@1.11.0")
    depends_on("mpi", when="+mpi")

    depends_on("openblas threads=openmp", when="+openmp ^[virtuals=blas] openblas")
    depends_on("blis threads=openmp", when="+openmp ^[virtuals=blas] blis")
    depends_on("amdblis threads=openmp", when="+openmp ^[virtuals=blas] amdblis")

    extends("python", when="+python")

    with when("+cuda"):
        depends_on("cufinufft+cuda")
        # propagate cuda arch requirement
        for val in CudaPackage.cuda_arch_values:
            depends_on(f"cufinufft+cuda cuda_arch={val}", when=f"cuda_arch={val}")

    with when("+python"):
        depends_on("python@3.8:")
        depends_on("py-pybind11", type="build")
        depends_on("py-numpy")
        depends_on("py-astropy")
        depends_on("py-casacore")
        depends_on("py-matplotlib")
        depends_on("py-tqdm")
        depends_on("py-pyproj")
        depends_on("py-healpy")
        depends_on("py-scikit-learn")
        depends_on("py-pandas")
        depends_on("py-scipy")


    def cmake_args(self):
        args = [
            "-DBIPP_BUNDLED_LIBS=OFF",
            self.define_from_variant("BIPP_OMP", "openmp"),
            self.define_from_variant("BIPP_PYTHON", "python"),
            self.define_from_variant("BIPP_MPI", "mpi"),
        ]

        if self.spec.satisfies("+python"):
            args += [
                "-DBIPP_INSTALL_PYTHON_PREFIX=" + python_platlib,
                "-DBIPP_INSTALL_PYTHON_SUFFIX=",
            ]

        if self.spec.satisfies("+cuda"):
            args += ["-DBIPP_GPU=CUDA"]

            cuda_arch = self.spec.variants["cuda_arch"].value
            if cuda_arch[0] != "none":
                args += [self.define("CMAKE_CUDA_ARCHITECTURES", cuda_arch)]
        else:
            args += ["-DBIPP_GPU=OFF"]

        return args

