CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

rez_find_packages(PREFIX pkgs AUTO)
set(ocio_version ${OCIO_VERSION})

set(url_ocio https://github.com/imageworks/OpenColorIO.git)
set(tag_ocio v${ocio_version})


if(${REZ_BUILD_INSTALL})
    set(install_cmd rez-env -i ${PROJECT_BINARY_DIR}/build.rxt -- make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    ocio
    GIT_REPOSITORY ${url_ocio}
    GIT_TAG ${tag_ocio}
    PREFIX ocio
    INSTALL_COMMAND "${install_cmd}"
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DPYTHON_INCLUDE_DIR=${PYTHON_INCLUDE_DIRS} -DPYTHON_LIBRARY=${PYTHON_LIBDIR}/lib${PYTHON_LIBRARIES}.so
)
