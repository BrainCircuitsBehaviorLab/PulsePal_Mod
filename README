# Pulse Pal Mod

This repository provides a **modified version** of the Pulse Pal firmware and
Python API.

Original project by Sanworks LLC:
https://github.com/sanworks/PulsePal

---

## New Features in This Mod

1. **Ramps**:
   Whenever an output channel activated by a trigger is stopped externally
   (for example, by a second trigger in toggle mode or by the signal going low in
   pulse-gated mode),the channel ramps smoothly from its current voltage down to the
   defined resting voltage, using the programmed ramp duration.

2. **Persistent custom trains**:
   Originally, Pulse Pal allowed storing 2 custom trains or waveforms in memory,
   but they were erased on reset.
   With this modification, custom trains are stored persistently and can be used
   in **standalone mode** (running only on power, without a PC or Raspberry Pi
   connection).

---

## How to Use

### 1. Clone this repository

### 2. Update Pulse Pal firmware

1. Download and install Arduino from:
https://www.arduino.cc/en/Main/Software
2. Launch Arduino
3. Open the boards manager from the left-hand toolbar.
4. Under "Arduino SAM Boards (32-bits ARM Cortex-M3)", if it is not already installed,
choose "Install"
5. Close the boards Manager.
6. Download the latest release of SDFat library version 1, extract it and put it in
/Documents/Arduino/libraries/
7. Select: File > Open and choose /PulsePal/Firmware/PulsePal_Mod/PulsePal_Mod.ino
8. Select Tools > Board > Arduino Due (Native USB Port)
9. Select Tools > Port > (whichever port appears when you connect Pulse Pal, and
disappears when it is
disconnected)
10. Press "Upload" - the right-pointing arrow below in the first toolbar above the code
If all goes well, after a few seconds you should see some orange text in the black
console window that
says
   `"Verify successful... CPU reset."`

### 3. Configure Pulse Pal

- Read the
[Pulse Pal Wiki](https://sites.google.com/site/pulsepalwiki/pulse-pal?authuser=0)
for a description of the parameters and commands.
- Read carefully the included [example.py](example.py) for guidance.
- Write your own Python script to configure channels and triggers.
- If you define custom trains (2 slots available), they will be **saved automatically**
with the rest of your parameters when you call `saveSDSettings` at the end of your
script.
- Connect Pulse Pal to your computer or Raspberry Pi.
- Identify its serial port and update the `address` variable in your script.
- Run your script to apply configuration.
- Now you can disconnect the Pulse Pal from the computer and use it in
**standalone mode**.

### 4. Run standalone
- Connect your Pulse Pal to a power supply.
- Configurations can be reloaded:
  - From Python using `loadSettings`
  - Directly from the Pulse Pal joystick
  - If your configuration was saved as **default.pps**, the configuration will load
  automatically every time the device powers on.

---

## IMPORTANT NOTES

- Always verify pulses with an **oscilloscope** before experimental use.
- You may first test them using the joystick to manually trigger pulses, but you should
always run a final test with the actual Bpod task and Bpod-generated triggers to ensure
full compatibility.
