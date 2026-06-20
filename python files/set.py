def print_lyrics():
    num_lines = min(len(lyrics),len(delays))
    for i in range(num_lines):
        line = lyrics[i]

        #---Typing Effect Implementation...
        for char in line:
            print(char,end='',flush=True)
            time.sleep(CHAR_DELAY)

        print()


print()