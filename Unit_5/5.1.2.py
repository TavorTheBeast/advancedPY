import winsound

freqs = {
    "la": 220,
    "si": 247,
    "do": 261,
    "re": 293,
    "mi": 329,
    "fa": 349,
    "sol": 392,
}

notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

# Split the notes string by hyphen to get individual notes
note_list = notes.split("-")

# Iterate over the notes and play each one
for note in note_list:
    # Split the note into its frequency and duration parts
    note_parts = note.split(",")
    frequency = freqs[note_parts[0]]  # Get the frequency from the dictionary
    duration = int(note_parts[1])  # Convert the duration to an integer

    # Play the note using winsound.Beep
    winsound.Beep(frequency, duration)
