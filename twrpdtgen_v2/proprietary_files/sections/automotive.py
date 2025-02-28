# BACKUP REPLACE FILE

#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from twrpdtgen_v2.proprietary_files.section import Section, register_section

class AutomotiveSection(Section):
	name = "Automotive"
	interfaces = [
		"android.hardware.automotive.audiocontrol",
		"android.hardware.automotive.can",
		"android.hardware.automotive.evs",
		"android.hardware.automotive.occupant_awareness",
		"android.hardware.automotive.sv",
		"android.hardware.automotive.vehicle",
		"vendor.qti.hardware.automotive.vehicle",
	]

register_section(AutomotiveSection)
