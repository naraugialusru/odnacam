# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled/cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/test_leet14.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/test_leet14.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/test_leet14.dir/flags.make

CMakeFiles/test_leet14.dir/leet1672.cpp.o: CMakeFiles/test_leet14.dir/flags.make
CMakeFiles/test_leet14.dir/leet1672.cpp.o: ../leet1672.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/test_leet14.dir/leet1672.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test_leet14.dir/leet1672.cpp.o -c "/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled/leet1672.cpp"

CMakeFiles/test_leet14.dir/leet1672.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_leet14.dir/leet1672.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled/leet1672.cpp" > CMakeFiles/test_leet14.dir/leet1672.cpp.i

CMakeFiles/test_leet14.dir/leet1672.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_leet14.dir/leet1672.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled/leet1672.cpp" -o CMakeFiles/test_leet14.dir/leet1672.cpp.s

CMakeFiles/test_leet14.dir/tests/test_leet1672.cpp.o: CMakeFiles/test_leet14.dir/flags.make
CMakeFiles/test_leet14.dir/tests/test_leet1672.cpp.o: ../tests/test_leet1672.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/test_leet14.dir/tests/test_leet1672.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test_leet14.dir/tests/test_leet1672.cpp.o -c "/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled/tests/test_leet1672.cpp"

CMakeFiles/test_leet14.dir/tests/test_leet1672.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_leet14.dir/tests/test_leet1672.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled/tests/test_leet1672.cpp" > CMakeFiles/test_leet14.dir/tests/test_leet1672.cpp.i

CMakeFiles/test_leet14.dir/tests/test_leet1672.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_leet14.dir/tests/test_leet1672.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled/tests/test_leet1672.cpp" -o CMakeFiles/test_leet14.dir/tests/test_leet1672.cpp.s

# Object files for target test_leet14
test_leet14_OBJECTS = \
"CMakeFiles/test_leet14.dir/leet1672.cpp.o" \
"CMakeFiles/test_leet14.dir/tests/test_leet1672.cpp.o"

# External object files for target test_leet14
test_leet14_EXTERNAL_OBJECTS =

test_leet14: CMakeFiles/test_leet14.dir/leet1672.cpp.o
test_leet14: CMakeFiles/test_leet14.dir/tests/test_leet1672.cpp.o
test_leet14: CMakeFiles/test_leet14.dir/build.make
test_leet14: CMakeFiles/test_leet14.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable test_leet14"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_leet14.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/test_leet14.dir/build: test_leet14

.PHONY : CMakeFiles/test_leet14.dir/build

CMakeFiles/test_leet14.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/test_leet14.dir/cmake_clean.cmake
.PHONY : CMakeFiles/test_leet14.dir/clean

CMakeFiles/test_leet14.dir/depend:
	cd "/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled/cmake-build-debug" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled" "/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled" "/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled/cmake-build-debug" "/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled/cmake-build-debug" "/Users/pcc33/Google Drive/naraugialusru_git/odnacam/CLionProjects/untitled/cmake-build-debug/CMakeFiles/test_leet14.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/test_leet14.dir/depend
