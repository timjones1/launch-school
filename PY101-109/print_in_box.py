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

print_in_box("test string")

print_in_box("")