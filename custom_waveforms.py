import math

# helper functions to create custom waveforms

def create_square_pulse_with_ramps(
    duration, duration_ramp_in, duration_ramp_off, voltage, samples_per_second=1000
):
    duration_samples = int(duration * samples_per_second)
    duration_ramp_in_samples = duration_ramp_in * samples_per_second
    duration_ramp_off_samples = duration_ramp_off * samples_per_second
    start_ramp_off_samples = duration_samples - duration_ramp_off_samples
    voltages = list(range(0, duration_samples))
    for i in voltages:
        if i < duration_ramp_in_samples:
            voltages[i] = i * voltage / duration_ramp_in_samples
        elif i > start_ramp_off_samples:
            voltages[i] = (
                voltage
                - (i - start_ramp_off_samples) * voltage / duration_ramp_off_samples
            )
        else:
            voltages[i] = voltage
    return voltages


def create_sine_wave(
    duration, frequency, amplitude, offset=0, samples_per_second=1000
):
    duration_samples = int(duration * samples_per_second)
    voltages = list(range(0, duration_samples))
    for i in voltages:
        voltages[i] = offset + amplitude * math.sin(
            2 * math.pi * frequency * (i / samples_per_second)
        )
    return voltages
