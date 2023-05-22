class MusicNotes:
    def __init__(self):
        self.notes = {
            "la": [55, 110, 220, 440, 880],
            "si": [61.74, 123.48, 246.96, 493.92, 987.84],
            "do": [65.41, 130.82, 261.64, 523.28, 1046.56],
            "re": [73.42, 146.84, 293.68, 587.36, 1174.72],
            "mi": [82.41, 164.82, 329.64, 659.28, 1318.56],
            "fa": [87.31, 174.62, 349.24, 698.48, 1396.96],
            "sol": [98, 196, 392, 784, 1568]
        }
        self.notes_iter = self.generate_notes()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.notes_iter)

    def generate_notes(self):
        for note, frequencies in self.notes.items():
            for frequency in frequencies:
                yield frequency


notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)
