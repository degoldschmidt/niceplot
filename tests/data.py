def generate_data(dim):
    ### Generating fake example data
    categories = ['A','C','A','B','C']
    states = [False,False,True,True,True]
    listdfs = []
    means = [0.1, 0.1, 0.3, 1.5, 2.]
    stds = [0.1, 0.15, 0.25, 0.7, 1.]
    siz = 20
    for ix, acat in enumerate(categories[:dim]):
        y = np.clip(stds[ix]*np.random.randn(siz)+means[ix], 0, None)
        dfdict = {}
        dfdict['category'] = [acat]*siz
        dfdict['value'] = y
        dfdict['state'] = [states[ix]]*siz
        listdfs.append(pd.DataFrame(dfdict))
    return pd.concat(listdfs, ignore_index=True)
