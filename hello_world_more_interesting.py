from time import sleep
text = input()
first_letter = 20
current_text = []
for a in range(len(text)):
    current_text.append(" ")
for i in range(len(text)):
    current_letter = ord(text[i].lower())
    new_letter = first_letter
    while True:
        if new_letter == current_letter:
            current_text[i] = chr(new_letter)
            print(''.join(current_text))
            break
        current_text[i] = chr(new_letter)
        new_letter += 1
        sleep(0.0001)
        print(''.join(current_text))



