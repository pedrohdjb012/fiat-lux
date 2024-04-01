def on_forever():
    if input.light_level() > 100:
        basic.show_leds("""
            # . # . #
            . # # # .
            # # # # #
            . # # # .
            # . # . #
            """)
    else:
        basic.clear_screen()
basic.forever(on_forever)
