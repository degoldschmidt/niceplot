if __name__ == "__main__":
    import pandas as pd
    ### some data
    colors = ['#dd1c77', '#f9c6dd', '#2ca25f', '#99d8b3', '#b9eec3']
    many_df = [generate_data(4) for i in range(6)]

    # The actual magic
    f, axes = plt.subplots(2,3, figsize=(8,6), dpi=300)
    print(f.get_size_inches())
    ix = 0
    for row in axes:
        for ax in row:
            ax = swarmbox(x=['state', 'category'], y='value', data=many_df[ix], colors=colors, ax=ax)
            ix += 1
    f.suptitle('Careful, this is artificial data!')
    #plt.show()
    f.savefig("here.pdf")
