##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
##########################################################################
# Copyright (c) 2015-2017 Krell Institute. All Rights Reserved.
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA  02111-1307  USA
##########################################################################

from spack import *


class CbtfLanl(CMakePackage):
    """CBTF LANL project contains a memory tool and data center type system
       command monitoring tool."""
    homepage = "http://sourceforge.net/p/cbtf/wiki/Home/"

    version('1.8', branch='master',
            git='http://git.code.sf.net/p/cbtf-lanl/cbtf-lanl')

    depends_on("cmake@3.0.2:", type='build')
    # Dependencies for cbtf-krell
    depends_on("mrnet@5.0.1:+lwthreads")
    depends_on("xerces-c@3.1.1:")
    depends_on("cbtf")
    depends_on("cbtf-krell")

    parallel = False

    build_directory = 'build_cbtf_lanl'

    def build_type(self):
        return 'None'

    def cmake_args(self):

        spec = self.spec
        compile_flags = "-O2 -g"

        cmake_args = [
            '-DCMAKE_CXX_FLAGS=%s'        % compile_flags,
            '-DCMAKE_C_FLAGS=%s'          % compile_flags,
            '-DCBTF_DIR=%s'               % spec['cbtf'].prefix,
            '-DCBTF_KRELL_DIR=%s'         % spec['cbtf-krell'].prefix,
            '-DMRNET_DIR=%s'              % spec['mrnet'].prefix,
            '-DXERCESC_DIR=%s'            % spec['xerces-c'].prefix,
            '-DCMAKE_MODULE_PATH=%s'      % join_path(
                prefix.share, 'KrellInstitute', 'cmake')]

        return cmake_args
