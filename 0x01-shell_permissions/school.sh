#!/bin/bash
for file in "$@"; do file -m school.mgc "$file"; done
