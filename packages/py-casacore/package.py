from spack.package import *


class PyCasacore(PythonPackage):
    """Casacore Python bindings"""

    homepage = "https://github.com/casacore/python-casacore"
    pypi = "python-casacore/python-casacore-3.5.2.tar.gz"

    license("LGPL")

    version("3.5.2", sha256="ad70c8e08893eec928b3e38c099bda8863f5aa9d099fd00694ad2b0d48eba08f")
    version("3.5.1", sha256="a577233c7311f64a8048180ee82d6946fee16e0dce2976eb516784a32d8b9133")
    version("3.5.0", sha256="47ac85d47051074d64415414212c8c2cfcb49a2037f5c3d78f71ab5b162d1e8b")
    version("3.4.0", sha256="f654781292308de70c037981f5f7f5aeb02cf980a6f1367d1c294e7b4fca42ce")
    version("3.3.1", sha256="c1f196b87ea34f930da6900eebc0a8f39291352d4def6631a2ec148ef5cf083a")
    version("3.3.0", sha256="e682940c50e6dbeb4e4a3301e3e15cd89774ce6849dfc1b6602b6663c058213b")
    version("3.2.0", sha256="d48e6202831ef22983961aa14c82294325f71b2fd3e108efaa3c1ca99b7505b5")
    version("3.1.1", sha256="4f1cb747ff8d1fc93bd8405bdbe2404e92105be52e14c5152fc2552714fb17ee")
    version("3.0.0", sha256="d0fd963ef54c6eec707a3760965d65da3e3afbd11f67fe8f810ba0887cb3140d")

    depends_on("py-setuptools", type="build")
    depends_on("boost+python", type=("build"))
    depends_on("casacore+python", type=("build", "run"))
    depends_on("wcslib")
    depends_on("cfitsio")


    def setup_build_environment(self, env):
        # search path used by install script
        env.prepend_path("LD_LIBRARY_PATH", self.spec["boost"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["casacore"].prefix.lib)
        # required headers from casacore
        env.prepend_path("CPLUS_INCLUDE_PATH", self.spec["wcslib"].prefix.include)
        env.prepend_path("CPLUS_INCLUDE_PATH", self.spec["cfitsio"].prefix.include)
