# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class HealpixCxx(AutotoolsPackage):
    """Healpix-CXX is a C/C++ library for calculating
    Hierarchical Equal Area isoLatitude Pixelation of a sphere."""

    homepage = "https://healpix.sourceforge.io"
    url = "https://deac-ams.dl.sourceforge.net/project/healpix/Healpix_3.82/healpix_cxx-3.82.0.tar.gz"

    license("GPL-2.0-or-later")

    version("3.82.0", sha256="9c1b0bbbcf007359d1ef10ae3ae9a2f46c72a4eb0c2fdbb43683289002ba8552")
    version("3.50.0", sha256="6538ee160423e8a0c0f92cf2b2001e1a2afd9567d026a86ff6e2287c1580cb4c")

    depends_on("cfitsio@4:", when="@3.82.0")
    depends_on("cfitsio@:3", when="@3.50.0")
    depends_on("libsharp@1.1.0 ~mpi", type="build")
    depends_on("pkg-config", type="build")

    #  def patch(self):
    #      spec = self.spec
    #      configure_fix = FileFilter("configure")
    #      # Link libsharp static libs
    #      configure_fix.filter(
    #          r"^SHARP_LIBS=.*$",
    #          'SHARP_LIBS="-L{0} -lsharp -lc_utils -lfftpack -lm"'.format(
    #              spec["libsharp"].prefix.lib
    #          ),
    #      )

    def setup_build_environment(self, env):
        env.append_flags("CPPFLAGS", self.spec["libsharp"].headers.include_flags)
        env.append_flags("CFLAGS", self.spec["libsharp"].headers.include_flags)
        env.append_flags("LDFLAGS", "-L{0} -Wl,-rpath,{0}".format(self.spec["libsharp"].libs.directories[0]))
