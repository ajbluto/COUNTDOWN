# COUNTDOWN

A simple Tkinter countdown widget that displays the time remaining until February 5th of the upcoming year.

## Features

- **Always on top**: The widget stays visible above other windows
- **No window decorations**: Clean, minimal appearance
- **Draggable**: Click and drag the widget to move it around the screen
- **Auto-updating**: Updates every second with precise countdown
- **Year rollover**: Automatically targets next year's February 5th if the current date has passed
- **Styled display**: Lime green text on black background in a clear format

## Usage

Run the countdown widget:

```bash
python3 countdown_widget.py
```

The widget will display the countdown in the format: `Xd XXh XXm XXs`
- `Xd` = days remaining
- `XXh` = hours remaining (00-23)
- `XXm` = minutes remaining (00-59)
- `XXs` = seconds remaining (00-59)

## Requirements

- Python 3.x
- tkinter (usually included with Python)

On Ubuntu/Debian systems, if tkinter is not available:
```bash
sudo apt install python3-tk
```

## Controls

- **Drag**: Click anywhere on the widget and drag to move it
- **Close**: Use your window manager or terminate the Python process

The widget will automatically position itself in the center of the screen when started.
