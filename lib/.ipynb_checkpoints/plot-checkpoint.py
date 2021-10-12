import matplotlib.pyplot as plt


def plot(data, rolling=0, xlabel='Date', ylabel=None):
    if(rolling == 0):
        plot_basic(data, xlabel, ylabel)
    else:
        plot_rolling(data, rolling, xlabel, ylabel)


def plot_basic(data, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(16,9))
    ax.plot(data.index, data['Adj Close'])

    if(xlabel):
        ax.set_xlabel(xlabel)
        
    if(ylabel):
        ax.set_ylabel(ylabel)

    
def plot_rolling(data, rolling, xlabel, ylabel):
    data_rolled = data.rolling(window=rolling).mean()
    
    plot_basic(data_rolled, xlabel, ylabel)
    
    
