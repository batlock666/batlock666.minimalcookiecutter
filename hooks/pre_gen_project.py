# NOQA: D100

import sys

package_name = "{{ cookiecutter.subpackage }}".strip()

if not package_name:
    print("ERROR: no subpackage given")
    sys.exit(1)
