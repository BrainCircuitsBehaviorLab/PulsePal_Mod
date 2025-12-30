from PulsePal import PulsePalObject

# this file contains a real case of use in our lab
# in this case, we configure the PulsePal to generate
# 4 different pulse trains all triggered by the same trigger channel
# the first train is a single long pulse with ramp down
# the other trains are pulse trains of varying frequencies
# all trains are pulse-gated, meaning that they start when the trigger goes high
# and stop when the trigger goes low


# ---- CREATE PULSE PAL OBJECT ----
# Update with the correct serial port address for your system.
address = "/dev/tty.usbmodem1301"
pulse_pal = PulsePalObject(address)


# ---- CLEAR EXISTING SETTINGS ----
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






# ---- TRIGGER CHANNEL 1 ---- OUTPUT CHANNEL 1 ---- SINGLE PULSE WITH RAMP ----
# 1) Create a 30 s monophasic 5 V pulse on output channel 1.
# Because this train contains a single pulse, the train duration must match
# the pulse duration (phase1Duration).
trigger_channel = 1
output_channel = 1
voltage = 5  # volts
duration = 30  # seconds

pulse_pal.programOutputChannelParam("phase1Voltage", output_channel, voltage)
pulse_pal.programOutputChannelParam("phase1Duration", output_channel, duration)
pulse_pal.programOutputChannelParam("pulseTrainDuration", output_channel, duration)

# 2) Enable ramp-down on output channel 1 and set ramp duration to 0.5 s.
pulse_pal.setRampEnabled(output_channel, True)
pulse_pal.setRampDuration(output_channel, 0.5)  # seconds

# 3) Link trigger channel 1 to output channel 1 (0 = not linked, 1 = linked).
pulse_pal.programOutputChannelParam("linkTriggerChannel1", output_channel, 1)

# 4) Set trigger channel 1 to pulse-gated mode
# (0 = normal, 1 = toggle, 2 = pulse-gated).
pulse_pal.programTriggerChannelParam("triggerMode", trigger_channel, 2)





# ---- TRIGGER CHANNEL 2 ---- OUTPUT CHANNEL 2 ---- SINGLE PULSE WITH RAMP ----
# 1) Create a 30 s monophasic 5 V pulse on output channel 2.
# Because this train contains a single pulse, the train duration must match
# the pulse duration (phase1Duration).
trigger_channel = 2
output_channel = 2
voltage = 5  # volts
duration = 30  # seconds

pulse_pal.programOutputChannelParam("phase1Voltage", output_channel, voltage)
pulse_pal.programOutputChannelParam("phase1Duration", output_channel, duration)
pulse_pal.programOutputChannelParam("pulseTrainDuration", output_channel, duration)

# 2) Enable ramp-down on output channel 2 and set ramp duration to 0.5 s.
pulse_pal.setRampEnabled(output_channel, True)
pulse_pal.setRampDuration(output_channel, 0.5)  # seconds

# 3) Link trigger channel 2 to output channel 2 (0 = not linked, 1 = linked).
pulse_pal.programOutputChannelParam("linkTriggerChannel2", output_channel, 1)

# 4) Set trigger channel 2 to pulse-gated mode
# (0 = normal, 1 = toggle, 2 = pulse-gated).
pulse_pal.programTriggerChannelParam("triggerMode", trigger_channel, 2)



# ---- TRIGGER CHANNEL 1 ---- OUTPUT CHANNEL 3 ---- PULSE TRAIN ----
# 1) Program a 5 V pulse train in channel 3 at 20 Hz for a total duration of 30 s.
# Since 20 Hz means 20 cycles per second, each cycle lasts 1 / 20 = 0.05 s (50 ms).
# Within each 50 ms cycle, the signal should be ON for 5 ms and OFF for 45 ms. 10% ON.
trigger_channel = 1
output_channel = 3
voltage = 5  # volts
phase_duration = 0.005  # seconds
inter_pulse_interval = 0.045  # seconds
duration = 30  # seconds

pulse_pal.programOutputChannelParam("phase1Voltage", output_channel, voltage)
pulse_pal.programOutputChannelParam("phase1Duration", output_channel, phase_duration)
pulse_pal.programOutputChannelParam(
    "interPulseInterval", output_channel, inter_pulse_interval
)
pulse_pal.programOutputChannelParam("pulseTrainDuration", output_channel, duration)

# 2) Link trigger channel 1 to output channel 3 (0 = not linked, 1 = linked).
pulse_pal.programOutputChannelParam("linkTriggerChannel1", output_channel, 1)

# 3) Set trigger channel 1 is already pulse-gated from above



# ---- TRIGGER CHANNEL 2 ---- OUTPUT CHANNEL 4 ---- PULSE TRAIN ----
# 1) Program a 5 V pulse train in channel 4 at 20 Hz for a total duration of 30 s.
# Since 20 Hz means 20 cycles per second, each cycle lasts 1 / 20 = 0.05 s (50 ms).
# Within each 50 ms cycle, the signal should be ON for 5 ms and OFF for 45 ms. 10% ON.
trigger_channel = 2
output_channel = 4
voltage = 5  # volts
phase_duration = 0.005  # seconds
inter_pulse_interval = 0.045  # seconds
duration = 30  # seconds

pulse_pal.programOutputChannelParam("phase1Voltage", output_channel, voltage)
pulse_pal.programOutputChannelParam("phase1Duration", output_channel, phase_duration)
pulse_pal.programOutputChannelParam(
    "interPulseInterval", output_channel, inter_pulse_interval
)
pulse_pal.programOutputChannelParam("pulseTrainDuration", output_channel, duration)

# 2) Link trigger channel 2 to output channel 4 (0 = not linked, 1 = linked).
pulse_pal.programOutputChannelParam("linkTriggerChannel2", output_channel, 1)

# 3) Set trigger channel 2 is already pulse-gated from above





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
