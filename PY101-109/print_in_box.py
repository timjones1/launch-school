def print_in_box(box_string):

    width = len(box_string) + 2

    dashed_border = "+" + "-" * width + "+"
    spaced_section = "|" + " " * width + "|"
    main_text = "| " + box_string + " |"

    print(dashed_border)
    print(spaced_section)
    print(main_text)
    print(spaced_section)
    print(dashed_border)


def trunc_print_in_box(box_string, max_width):

    width = min(max_width - 2,len(box_string) + 2) 

    dashed_border = "+" + "-" * width + "+"
    spaced_section = "|" + " " * width + "|"
    main_text = "| " + box_string[:width - 2] + " |"

    print(dashed_border)
    print(spaced_section)
    print(main_text)
    print(spaced_section)
    print(dashed_border)

trunc_print_in_box("hello my name is Guido", 12)

from math import ceil

def split_message_into_lines(message, message_width):
           
    nr_lines = ceil(len(message) / message_width)
    nr_pad_spaces = len(message) % message_width

    #pad message to full width on final line
    message = message + " " * nr_pad_spaces

    line_end = message_width
    message_in_lines = []

    while message:
        message_in_lines.append(message[:line_end])
        message = message[line_end:]

    return message_in_lines

def wrap_print_in_box(input_message, max_length):
    
    line_width = min(max_length - 4,len(input_message) + 2)
    pad_width = line_width + 2

    message_list = split_message_into_lines(input_message, line_width)

    dashed_line = "+" + "-" * pad_width + "+"
    spaced_line = "|" + " " * pad_width + "|"
    
    print(dashed_line)
    print(spaced_line)

    for message_line in message_list:
        print(f"| {message_line} |")
    
    print(spaced_line)
    print(dashed_line)

wrap_print_in_box("hello my name is Guido", 8)