import time

def print_lyrics():
    lines = [
        "so imma love you every night like it's the last night",
        "like it's the last night",
        "if the world is ending",
        "i would wanna be next to you",
        "if the party was over",
        "and our time on earth was through",
        "i would hold you just for a while",
        "and die with a smile",
        "if the world was ending",
        "i would wanna be next to you",
        "right next to you",
    ]
    
    delays = [0.6, 0.7, 1.0, 4.6, 1.0, 3.6, 1.7, 2.0, 0.9, 1.2, 0.5]
    
    for i, line in enumerate(lines):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.1)  # short delay for character printing
        time.sleep(delays[i])  # delay between lines
        print()  # move to the next line

print_lyrics()  # Call the function to execute

