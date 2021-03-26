"""
Platform module

* Is used to retrieve as much possible information about the platform on which
  the program is being currently executed.
* Now by platform info, it means information about the device, it's OS, node,
  OS version, Python version, etc
* Reference: https://docs.python.org/3/library/platform.html
"""
import platform


###############################################################################
# Platform general information
###############################################################################


# architecture()
# * Queries the given executable (defaults to the Python interpreter binary)
#   for various architecture information
print(platform.architecture())
# ('64bit', 'WindowsPE')


# machine()
# * Returns the machine type, e.g. 'i386'.
# * An empty string is returned if the value cannot be determined
print(platform.machine())
# AMD64


# node()
# * Returns the computer’s network name
# * An empty string is returned if the value cannot be determined
print(platform.node())
# PC


# platform()
# * Returns a single string identifying the underlying platform with as much
#   useful information as possible
print(platform.platform())
# Windows-10-10.0.19041-SP0


# processor()
# * Returns the (real) processor name
print(platform.processor())
# Intel64 Family 6 Model 142 Stepping 12, GenuineIntel


# release()
# * Returns the system’s release
print(platform.release())
# 10


# system()
# * Returns the system/OS name
print(platform.system())
# Windows


# system_alias(system, release, version)
# * Returns (system, release, version) aliased to common marketing names used
#   for some systems
system = platform.system()
release = platform.release()
version = platform.version()
print(platform.system_alias(system, release, version))
# ('Windows', '10', '10.0.19041')


# version()
# * Returns the system’s release version
print(platform.version())
# 10.0.19041


# uname()
# * Fairly portable uname interface.
# * Returns a namedtuple() containing six attributes: system, node, release,
#   version, machine, and processor
print(platform.uname())
# uname_result(system='Windows', node='PCVINICIUS', release='10',
# version='10.0.19041', machine='AMD64')


###############################################################################
# Java Platform information
###############################################################################


# java_ver(release='', vendor='', vminfo=('', '', ''), osinfo=('', '', ''))
# * Version interface for Jython
# * Returns a tuple (release, vendor, vminfo, osinfo) with vminfo
# * Values which cannot be determined are set to the defaults given as
#   parameters (which all default to '')
print(platform.java_ver())
# ('', '', ('', '', ''), ('', '', ''))  # Cannot be determinated


###############################################################################
# Windows Platform information
###############################################################################


# win32_ver()
# * Get additional version information from the Windows Registry and return a
#   tuple (release, version, csd, ptype) referring to OS release, version
#   number, CSD level (service pack) and OS type (multi/single processor)
print(platform.win32_ver())
# ('10', '10.0.19041', 'SP0', 'Multiprocessor Free')


# win32_edition()
# * Returns a string representing the current Windows edition
print(platform.win32_edition())
# Enterprise


# win32_is_iot()
# * Return True if the Windows edition returned by win32_edition() is
#   recognized as an IoT edition
print(platform.win32_is_iot())
# False


###############################################################################
# Mac Platform information
###############################################################################


# mac_ver()
# * Get Mac OS version information and return it as tuple (release,
#   versioninfo, machine) with versioninfo being a tuple (version, dev_stage,
#   non_release_version)
print(platform.mac_ver())
# ('', ('', '', ''), '')


###############################################################################
# Unix Platform information
###############################################################################


# libc_ver()
# * Tries to determine the libc version against which the file executable
#   (defaults to the Python interpreter) is linked
# * Returns a tuple of strings (lib, version) which default to the given
#   parameters in case the lookup fails
print(platform.libc_ver())
# ('', '')
