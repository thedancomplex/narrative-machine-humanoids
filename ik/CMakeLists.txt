cmake_minimum_required (VERSION 2.6)
project (AminoTutorials)

# pkg-config setup
find_package(PkgConfig)

# Search for the pkg-config packages
pkg_search_module(SDL2 REQUIRED sdl2)
pkg_search_module(GL REQUIRED gl)
pkg_search_module(AMINO REQUIRED amino)
pkg_search_module(AMINO_GL REQUIRED amino-gl)

# Compile scene graph to C
add_custom_command(
  OUTPUT mallot-darwin.c mallot-darwin.c.h
  DEPENDS scene.robray
  COMMAND aarxc "scene.robray" -o mallot-darwin.c -n "music"
  )

# Compile plugin (shared library)
add_library( music MODULE mallot-darwin.c )
target_include_directories( music PUBLIC
  ${AMINO_INCLUDE_DIRS}
  )
target_link_libraries( music
  ${AMINO_GL_LIBRARIES}
  ${AMINO_LIBRARIES}
  )
