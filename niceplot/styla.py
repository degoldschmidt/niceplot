import os, sys
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.table as mpl_table
import matplotlib.text as mpl_text

def set_font(name, ax=None):
    if ax is None:
        ax = plt.gca()
    for sites in sys.path:
        if os.path.isdir(sites):
            if "fonts" in [folder for folder in os.listdir(sites) if os.path.isdir(os.path.join(sites,folder))]:
                fontfile = os.path.join(sites, "fonts", name+".ttf")

    if os.path.exists(fontfile):
        print("Loading font:", fontfile)
        textprop = fm.FontProperties(fname=fontfile)

        texts = ax.findobj(match=mpl_text.Text)
        print(texts)

        ### titles/labels
        ax.set_title(ax.get_title(), fontproperties=textprop)
        ax.set_xlabel(ax.get_xlabel(), fontproperties=textprop)
        ax.set_ylabel(ax.get_ylabel(), fontproperties=textprop)
        ### ticks
        for label in ax.get_xticklabels():
            label.set_fontproperties(textprop)
        for label in ax.get_yticklabels():
            label.set_fontproperties(textprop)
        ### legend
        if not ax.get_legend() is None:
            for text in ax.get_legend().get_texts():
                text.set_fontproperties(textprop)
        ### table
        tables = ax.findobj(match=table.Table)
        for eachtable in tables:
            for k, cell in eachtable._cells.items():
                this_text = cell._text.get_text()
                if this_text == u"\u25CF" or this_text == u"\u25CB":
                    cell._text.set_fontname("Arial Unicode MS")
                else:
                    cell._text.set_fontproperties(textprop)
    else:
        print(fontfile, os.getcwd())
        print("[ERROR]: selected font does not exist.")
        raise FileNotFoundError
    return ax


### table
"""

"""
