from spack.package import *

class Finufft(MakefilePackage):
    """fiNUFFT"""

    homepage = "https://github.com/flatironinstitute/finufft"
    url = "https://github.com/flatironinstitute/finufft/archive/refs/tags/v2.1.0.tar.gz"
    git = "https://github.com/flatironinstitute/finufft.git"

    version("2.1.0", sha256="52f25f0ace06a6dd514a29e728ad31e317b76631912bf0bc53cbf06355e24ad7")

    variant("openmp", default=True, description="Build with OpenMP support")

    depends_on("fftw-api")
    depends_on("fftw ~mpi +openmp precision=float,double", when="^[virtuals=fftw-api] fftw")
    depends_on("amdfftw ~mpi +openmp precision=float,double", when="^[virtuals=fftw-api] amdfftw")

    patch("makefile.patch")

    def edit(self, spec, prefix):
        makefile_inc = []
        makefile_inc.append("CC:={}".format(self.compiler.cc))
        makefile_inc.append("CXX:={}".format(self.compiler.cxx))

        makefile_inc.append("INCL:=-I{}".format(spec["fftw-api"].prefix.include))

        if "^[virtuals=fftw-api] fftw" in spec or "^[virtuals=fftw-api] amdfftw" in spec:
            # ld_flags does not contain _omp and single precision libs
            fft_libs = "-lfftw3 -lfftw3_omp -lfftw3f -lfftw3f_omp"
        else:
            fft_libs = spec["fftw-api"].libs.ld_flags

        makefile_inc.append("LIBS:=-Wl,--disable-new-dtags -L{0} -Wl,-rpath,{0} {1}".format(spec["fftw-api"].libs.directories[0], fft_libs))

        opt_flags = "-O3"
        if "%gcc" in spec:
            opt_flags += " -fcx-limited-range"


        makefile_inc.append("CFLAGS:={}".format(opt_flags))
        makefile_inc.append("CXXFLAGS:=$(CFLAGS)")

        if "+openmp" in spec:
            makefile_inc.append("OMP:=ON")
            makefile_inc.append("OMPFLAGS:={}".format((self.compiler.openmp_flag)))
        else:
            makefile_inc.append("OMP:=OFF")

        with open("make.inc", "w") as fh:
            fh.write("\n".join(makefile_inc))
            fh.write("\n")


    @property
    def build_targets(self):
        spec = self.spec
        return ["lib"]


    def install(self, spec, prefix):
        install_tree("lib", prefix.lib)
        install_tree("include", prefix.include)

