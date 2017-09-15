### general labels
    fontfile = "C:\\Windows\\Fonts\\Quicksand-Regular.ttf"
    print(sys.platform)
    if sys.platform == "darwin":
        fontfile = "/Users/degoldschmidt/Library/Fonts/Quicksand-Regular.ttf"
    print("Load font:", fontfile)
    textprop = fm.FontProperties(fname=fontfile)
    ax.set_ylabel(y, fontproperties=textprop, fontsize=12)
    for label in ax.get_yticklabels():
        label.set_fontproperties(textprop)


### table
        for k,v in condition_table._cells.items():
            this_text = condition_table._cells[k]._text.get_text()
            if this_text == u"\u25CF" or this_text == u"\u25CB":
                condition_table._cells[k]._text.set_fontname("Arial Unicode MS")
                condition_table._cells[k]._text.set_fontsize(24)
            else:
                condition_table._cells[k]._text.set_fontproperties(textprop)
