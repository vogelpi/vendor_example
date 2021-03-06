#!/usr/bin/env python3
# Copyright lowRISC contributors.
# Licensed under the Apache License, Version 2.0, see LICENSE for details.
# SPDX-License-Identifier: Apache-2.0

import subprocess
import glob

ot_dir = '../opentitan'

# Detect all vendored IPs
ip_list = glob.glob('*vendor.hjson')

# Vendor!
for ip in ip_list:
	print('vendoring ' + ip)
	cmd = [ot_dir + '/' + 'util/vendor.py', ip, '--commit']
	subprocess.run(cmd)

# https://github.com/lowRISC/stwg-base/issues/406
# Export patches:
## $ cd $STWG_BASE_TOP
## $ cd hw/vendor/lowrisc_ibex
## $ git format-patch --relative -o /tmp/patches origin/master
#Example:
# cd vendor
# git format-patch --relative -o patches/usbpe/ 266a91df0a0b330c79aee8edf038ac9f899c971a // commit when we did the last vendor in
# creates one patch per commit since then, patches are empty if not files in current dir affected
# adjust paths in patches to OT base

# Import patches (you must have the upstream repo somwhere):
#$ cd ~/src/upstream
#$ git fetch
#$ git checkout -b a-branch-name-for-your-features
#$ git am /tmp/patches/*.patch
