def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Print a string centered, with ** on either side.
    :param text: the string to print.
        An asterik (*) will result in a row of asteriks
        the default will print a blank line, with a ** border

    :param screen_width: the overall width to print within
    :raises ValueError: if the supplied string is too long
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}".format(text, screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*")
banner_text("Always look at the bright side of life...")
banner_text("if life seems jolly rotten,")
banner_text("Theres something you've forgotten")
banner_text(screen_width=60)
banner_text("Always look at the bright side of life...")
banner_text("if life seems jolly rotten,")
banner_text("Theres something you've forgotten")
banner_text("*")
