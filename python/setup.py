# -*- coding: utf-8 -*-
#
# This file is part of the CT2 project
#
# Copyright (c) : 2015
# Beamline Control Unit, European Synchrotron Radiation Facility
# BP 220, Grenoble 38043
# FRANCE
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.

def main():
    import os
    import sys
    
    setup_dir = os.path.dirname(os.path.abspath(__file__))

    # make sure we use latest info from local code
    sys.path.insert(0, setup_dir)

    from ct2 import release
    from distutils.core import setup

    packages = ["ct2", "ct2.tango", "ct2.tango.server"]

    setup(name=release.name, version=release.version,
          description=release.description,
          author=release.author,
          package_dir={release.name: release.name},
          packages=packages)


if __name__ == "__main__":
    main()
