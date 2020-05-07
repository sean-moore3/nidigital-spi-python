"""
Overview
This getting started example demonstrates how to use the NI-Digital Pattern Driver API to load pre-created files
with SPI pattern information on the NI Digital Pattern Instrument, burst the pattern,
and record the site pass/fail information.
"""

import nidigital

levels_sheet = 'PinLevels.digilevels'
timing_sheet = 'Timing.digitiming'

session = nidigital.Session("PXI1Slot2,PXI1Slot3", False, False, {"Simulate": True, "DriverSetup": {"Model": "6570"}})

# Load the pin map for the instrument at the beginning of the test program to reference pin names the pin map defines.
session.load_pin_map("PinMap.pinmap")

# Load the specifications, levels, and timing files you created in the Digital Pattern Editor on the instrument.
# # These settings are not applied until you call the apply_levels_and_timing.
session.load_specifications_levels_and_timing('Specifications.specs', levels_sheet, timing_sheet)

# Apply the settings from the levels and timing files you just loaded on the instrument.
session.apply_levels_and_timing(levels_sheet, timing_sheet)

# Load the pattern file (.digipat) you created in the Digital Pattern Editor on the instrument.
session.load_pattern('Pattern.digipat')

# Burst the pattern from the start label you specify,
# which can be a label in the .digipat pattern file or the name of the pattern.
print(session.burst_pattern('SPI_Pattern'))

# Disconnect all channels using programmable onboard switching.
session.selected_function = nidigital.SelectedFunction.DISCONNECT

# Close the session to the instrument.
session.close()
