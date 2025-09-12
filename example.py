from PulsePal import PulsePalObject
from custom_waveforms import create_square_pulse_with_ramps


# ---- PULSE PAL WIKI ----
# https://sites.google.com/site/pulsepalwiki/pulse-pal?authuser=0


# ---- PULSE PAL OVERVIEW ----
# The Pulse Pal has:
# - 4 output channels
# - 2 trigger channels
# - 2 custom train memory slots
#
# Output channels:
# Each of the 4 output channels can be programmed independently.
# An output channel can either:
#   - Generate pulse-trains (defined by voltage, duration, etc.), or
#   - Play one of the 2 custom trains stored in memory.
#
# Trigger channels:
# Each trigger channel can be configured independently.
# A single trigger channel can activate one or multiple output channels, and you can
# also define how each trigger responds to incoming pulses
# (normal, toggle, pulse-gated).
# - In normal mode, an incoming trigger (low to high logic transition) received by a
#   trigger channel will start pulse trains on all linked output channels.
#   Additional trigger pulses received during playback of the pulse train will be
#   ignored.
# - In toggle mode, an incoming trigger received by a trigger channel will start pulse
#   trains on linked output channels.
#   If an additional trigger pulse is detected during playback, the pulse trains on all
#   linked output channels are stopped.
# - In pulse gated mode, a low to high logic transition starts playback and a high to
#   low transition stops playback.
#
# Custom train slots:
# Each slot can store a custom pulse train or waveform, which can then be assigned
# to any of the 4 output channels.


# ---- CREATE PULSE PAL OBJECT ----
# Update with the correct serial port address for your system.
address = "/dev/tty.usbmodem1301"
pulse_pal = PulsePalObject(address)


# ---- CLEAR EXISTING SETTINGS ----
# IMPORTANT: Always clear channel configuration before programming new trains,
# otherwise values previously stored in Pulse Pal memory may persist.
for channel in range(1, 5):
    pulse_pal.programOutputChannelParam("isBiphasic", channel, 0)
    pulse_pal.programOutputChannelParam("phase1Voltage", channel, 0)
    pulse_pal.programOutputChannelParam("phase2Voltage", channel, 0)
    pulse_pal.programOutputChannelParam("phase1Duration", channel, 0)
    pulse_pal.programOutputChannelParam("phase2Duration", channel, 0)
    pulse_pal.programOutputChannelParam("interPhaseInterval", channel, 0)
    pulse_pal.programOutputChannelParam("interPulseInterval", channel, 0)
    pulse_pal.programOutputChannelParam("burstDuration", channel, 0)
    pulse_pal.programOutputChannelParam("interBurstInterval", channel, 0)
    pulse_pal.programOutputChannelParam("pulseTrainDuration", channel, 0)
    pulse_pal.programOutputChannelParam("pulseTrainDelay", channel, 0)
    pulse_pal.programOutputChannelParam("customTrainID", channel, 0)
    pulse_pal.programOutputChannelParam("customTrainTarget", channel, 0)
    pulse_pal.programOutputChannelParam("customTrainLoop", channel, 0)
    pulse_pal.programOutputChannelParam("restingVoltage", channel, 0)
    pulse_pal.programOutputChannelParam("linkTriggerChannel1", channel, 0)
    pulse_pal.programOutputChannelParam("linkTriggerChannel2", channel, 0)
    pulse_pal.setRampEnabled(channel, False)
    pulse_pal.setRampDuration(channel, 0)


# ---- OUTPUT CHANNEL 1 ----
# Goal:
# - A train containing a single monophasic pulse at 5 V with trial-dependent (variable)
#   duration.
# - Always end with a 0.1 s ramp-down to reduce rebound in neural responses.
#
# Rationale:
# Reprogramming the channel every trial to change duration would require keeping
# Pulse Pal connected to a computer. Instead, we program a sufficiently long pulse
# (30 s) and, on each trial, we start and stop it externally at the desired time.
# With ramp-down enabled, stopping the pulse smoothly returns it to the resting
# voltage (0 V) using the configured ramp duration (0.1 s).
#
# Triggering:
# Link output channel 1 to trigger channel 1, and set trigger channel 1 to
# pulse-gated mode. The output turns on when trigger 1 receives TTL high and turns
# off when the TTL goes low.
#
# Bpod usage:
# In Bpod, define a state machine with trial-dependent duration. While in that state,
# send TTL high to trigger channel 1. When the state ends, TTL goes low; Pulse Pal
# stops the output on channel 1 and applies the ramp-down if enabled.

# 1) Create a 30 s monophasic 5 V pulse on output channel 1.
# Because this train contains a single pulse, the train duration must match
# the pulse duration (phase1Duration).
output_channel = 1
voltage = 5  # volts
duration = 30  # seconds

pulse_pal.programOutputChannelParam("phase1Voltage", output_channel, voltage)
pulse_pal.programOutputChannelParam("phase1Duration", output_channel, duration)
pulse_pal.programOutputChannelParam("pulseTrainDuration", output_channel, duration)

# 2) Enable ramp-down on output channel 1 and set ramp duration to 0.1 s.
pulse_pal.setRampEnabled(output_channel, True)
pulse_pal.setRampDuration(output_channel, 0.1)  # seconds

# 3) Link output channel 1 to trigger channel 1 (0 = not linked, 1 = linked).
pulse_pal.programOutputChannelParam("linkTriggerChannel1", output_channel, 1)

# 4) Set trigger channel 1 to pulse-gated mode
# (0 = normal, 1 = toggle, 2 = pulse-gated).
trigger_channel = 1
pulse_pal.programTriggerChannelParam("triggerMode", trigger_channel, 2)


# ---- OUTPUT CHANNEL 2 ----
# Goal:
# - A train of monophasic pulses at 5 V.
# - Pulse width 0.001 s with 0.009 s between pulses.
# - Total train duration 5 s.
# - No ramp needed.
#
# Triggering:
# This train is linked to trigger channel 2. Since we do not need to stop it early,
# we can use normal mode: when Bpod sends a single pulse to trigger channel 2, the
# output plays the full 5 s train and then stops automatically.

# 1) Program a 5 V pulse of 0.1 s with 0.9 s between pulses; total train = 5 s.
output_channel = 2
voltage = 5  # volts
phase_duration = 0.001  # seconds
inter_pulse_interval = 0.009  # seconds
duration = 5  # seconds

pulse_pal.programOutputChannelParam("phase1Voltage", output_channel, voltage)
pulse_pal.programOutputChannelParam("phase1Duration", output_channel, phase_duration)
pulse_pal.programOutputChannelParam(
    "interPulseInterval", output_channel, inter_pulse_interval
)
pulse_pal.programOutputChannelParam("pulseTrainDuration", output_channel, duration)

# 2) Link output channel 2 to trigger channel 2 (0 = not linked, 1 = linked).
pulse_pal.programOutputChannelParam("linkTriggerChannel2", output_channel, 1)

# 3) Set trigger channel 2 to normal mode (0 = normal, 1 = toggle, 2 = pulse-gated).
trigger_channel = 2
pulse_pal.programTriggerChannelParam("triggerMode", trigger_channel, 0)


# ---- OUTPUT CHANNELS 3 & 4 ----
# Goal:
# - A train containing a fixed-duration monophasic pulse at 5 V lasting 3 s.
# - Include both a 0.1 s ramp-up and a 0.1 s ramp-down inside the waveform itself.
# - No external ramp-down needed because the waveform already ramps down.
#
# Waveform:
# To simulate a waveform we use a lot of samples. We need to specify the number
# of samples per second (here 1000) and the sample width (here 1 ms = 0.001 s).
# Be aware that the maximum number of samples per custom waveform is 10,000.
# Here we use 3 s * 1000 samples/s = 3000 samples, which is within the limit.
#
# Triggering:
# These channels will also be driven via trigger channel 2 (normal mode).

# 1) Build a custom waveform using a helper function:
# 3 s pulse with 0.1 s ramp-in and 0.1 s ramp-out.
duration = 3
duration_ramp_in = 0.1
duration_ramp_off = 0.1
voltage = 5
samples_per_second = 1000

voltages = create_square_pulse_with_ramps(
    duration, duration_ramp_in, duration_ramp_off, voltage, samples_per_second
)
sample_width = 1 / samples_per_second

# 2) Store the custom waveform (voltages and sample width) in custom train slot 1.
pulse_pal.sendCustomWaveform(1, sample_width, voltages)

# 3) Assign custom train 1 to output channels 3 and 4, and set the duration of
# the samples.
pulse_pal.programOutputChannelParam("customTrainID", 3, 1)
pulse_pal.programOutputChannelParam("phase1Duration", 3, sample_width)

pulse_pal.programOutputChannelParam("customTrainID", 4, 1)
pulse_pal.programOutputChannelParam("phase1Duration", 4, sample_width)

# 4) Link output channels 3 and 4 to trigger channel 2 (0 = not linked, 1 = linked).
pulse_pal.programOutputChannelParam("linkTriggerChannel2", 3, 1)
pulse_pal.programOutputChannelParam("linkTriggerChannel2", 4, 1)


# ---- SAVE SETTINGS ----
# Save configuration to a file (e.g., default.pps).
pulse_pal.saveSDSettings("default.pps")


# ---- CONFIRMATION ----
print("Pulse Pal configured successfully!")


# ---- IMPORTANT ----
# Always verify pulses with an oscilloscope before experimental use.
# You may first test them using the joystick to manually trigger pulses, but you should
# always run a final test with the actual Bpod task and Bpod-generated triggers to
# ensure full compatibility.
