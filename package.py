# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-anarci
#
# You can edit this file again by typing:
#
#     spack edit py-anarci
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyAnarci(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/oxpig"
    #git = "https://github.com/oxpig/ANARCI.git"
    git = "/workdir/ANARCI/.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    # license("UNKNOWN", checked_by="github_user1")

    # FIXME: Add proper versions and checksums here.
    version("1.3", branch="master")

    # FIXME: Add dependencies if required.
    depends_on("python@3.11.0", type=("build", "run"))
    depends_on("py-setuptools@58.2.0", type="build")
    depends_on("py-biopython@1.79")
    depends_on("hmmer@3.1b2")

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        super().install(spec, prefix)



