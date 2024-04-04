# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHealpy(PythonPackage):
    """healpy is a Python package to handle pixelated data on the sphere."""

    homepage = "https://healpy.readthedocs.io/"
    pypi = "healpy/healpy-1.13.0.tar.gz"

    license("GPL-2.0-only")

    version("1.16.6", sha256="0ab26e828fcd251a141095af6d9bf3dba43cec6f0f5cd48b65bf0af8f56329f1")
    version("1.16.5", sha256="9f99cd5ed2d8791dbfcefe1552a73e550ec85b87637127938756280008d0ed29")
    version("1.16.3", sha256="9fb7ad9c895fa399f814fcf69cafe13027edf8ab92f8d7ccb36e5c4c44f3d147")
    version("1.16.2", sha256="b7b9433152ff297f88fc5cc1277402a3346ff833e0fb7e026330dfac454de480")
    version("1.16.1", sha256="6d691b0a77fdf699672de09d39d82a640cfcc8ca03ae55022fb71e6edda69d2f")
    version("1.16.0", sha256="b13a47d90b1e467a4db6f6e2d24d6de46e140a9bc13f2e98b38fcda80d258e57")
    version("1.15.2", sha256="d559ad287a78d3b500919a5cb9e4dff3cb63c1b3a2e23edf62819c871ccacf7f")
    version("1.15.1", sha256="35de2b9e16189d31da34fadf9608d2a59d73ae5301ffdb6b4f99282bad4cb05f")
    version("1.15.0", sha256="e09300a9f24e40b07f09ca7a7026d640a0478960b6ca6a5fc85052c0bb4335bf")
    version("1.14.0", sha256="2720b5f96c314bdfdd20b6ffc0643ac8091faefcf8fd20a4083cedff85a66c5e")
    version("1.13.0", sha256="d0ae02791c2404002a09c643e9e50bc58e3d258f702c736dc1f39ce1e6526f73")
    version("1.7.4", sha256="3cca7ed7786ffcca70e2f39f58844667ffb8521180ac890d4da651b459f51442")

    depends_on("python@:3.10", type="build")
    depends_on("py-setuptools@3.2:", type="build")
    depends_on("py-pkgconfig", type="build")
    depends_on("py-numpy@1.13:", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-astropy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
    depends_on("cfitsio@4:", when="@1.16:", type=("build", "run"))
    depends_on("cfitsio@3:", when="@:1.15", type=("build", "run"))
    depends_on("healpix-cxx", type=("build", "run"))
    depends_on("libsharp ~mpi") # healpy-cxx dependency that defaults to mpi
    depends_on("py-cython@0.29.13:", type="build")
    depends_on("pkg-config", type="build")
