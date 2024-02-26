from spack.package import *


class PyAstropyIersData(PythonPackage):
    """Astropy data"""

    homepage = "https://github.com/astropy/astropy"
    pypi = "astropy-iers-data/astropy-iers-data-0.2024.3.25.0.29.50.tar.gz"

    version("0.2024.3.18.0.29.47", sha256="7ed8cbff91578a2c35eee787355fb24a3a2e891bc3af0551333727c0711cc0d5")
    version("0.2024.3.11.18.33.3", sha256="3c8ea9183c4a5e0ab6a85eef31197bbbc8cd20966e2249cf100cb7a604fc8a9c")
    version("0.2024.3.4.0.30.17", sha256="d530709e64d267a0547d305910608b8321f5d0225e37cf0b57430225b05114e2")
    version("0.2024.2.26.0.28.55", sha256="908d69c8b7ef9b644e4c8d3c8d22818f54f1ad5d364ab98b1eb1c57b7126abd3")

    license("BSD")

    depends_on("py-setuptools", type="build")
