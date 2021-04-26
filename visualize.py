import matplotlib.pyplot as plt
import numpy as np
import sys

rcconfig = {
    'figure.titlesize': 30,
    'figure.titleweight': 'bold',
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.major.width': 3,
    'ytick.major.width':3,
    'xtick.major.size': 9,
    'ytick.major.size': 9,
    'xtick.top': True,
    'ytick.right': True,
    'font.family': 'Times New Roman',
    'font.weight': 'bold',
    'font.size': 24,
    'mathtext.fontset': 'stix',
    'lines.linewidth': 3,
    'axes.linewidth': 3,
    'axes.formatter.use_mathtext': True,
    'axes.labelsize': 24,
    'axes.labelweight': 'bold',
    'axes.titleweight': 'bold',
}
plt.rcParams.update(rcconfig)


def plot(ed_pred, ed_true, sp_pred, sp_true, sli):
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))
    axes[0, 0].matshow(ed_pred[sli, :, :])
    axes[0, 1].matshow(ed_true[sli, :, :])
    axes[1, 0].matshow(sp_pred[sli, :, :])
    axes[1, 1].matshow(sp_true[sli, :, :])
    plt.show()

result_dir = '/home/luoxs/data_preperation/result/'
counter = sys.argv[1]
epoch = sys.argv[2]

# ElectronDensity
ed_pred = result_dir + 'ElectronDensity_Pred_'+str(counter)+'_'+str(epoch)+'.csv'
ed_true = result_dir + 'ElectronDensity_True_'+str(counter)+'_'+str(epoch)+'.csv'
# Species
sp_pred = result_dir + 'Species_True_'+str(counter)+'_'+str(epoch)+'.csv'
sp_true = result_dir + 'Species_Pred_'+str(counter)+'_'+str(epoch)+'.csv'

ed_pred = np.genfromtxt(ed_pred).reshape(30, 30, 30)
ed_true = np.genfromtxt(ed_true).reshape(30, 30, 30)
sp_pred = np.genfromtxt(sp_pred).reshape(30, 30, 30)
sp_true = np.genfromtxt(sp_true).reshape(30, 30, 30)
print(ed_pred.shape, ed_true.shape, sp_pred.shape, sp_true.shape)

for sli in range(10, 20):
    plot(ed_pred, ed_true, sp_pred, sp_true, sli)