# File to load in the periodic lattice data
# Code written by Jordan
from __future__ import print_function
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
import pickle
import numpy as np
from torch.utils.data.dataset import Dataset
from pymatgen.core.structure import Structure

directory = '/home/luoxs/data_preperation/'


class CrystalDataset(Dataset):
    #load input data.
    def __init__(self, lower=0, upper=1):
        print('Doing data loading now')
        options = range(32)
        self.input_data = np.vstack([
            pickle.load(open(
                directory + 'SAVE_Unit/Unit_' + str(options[n]) + '.pickle', 'rb'),
                        encoding='bytes') for n in range(lower, upper)
        ])
        print('Shape of Data is ', np.shape(self.input_data))

    def __getitem__(self, index):
        ID, electron, species, label, Zs, XYZs_shifted = self.input_data[index]
        species = np.array(species).astype(int)
        specie = np.zeros((95, 30, 30, 30))
        np.put_along_axis(specie, species[None, ...], 1, 0)
        cif_file = directory + 'crys_hoffmann/' + str(ID) + '.cif'
        crystal = Structure.from_file(cif_file)
        abc = np.array(crystal.lattice.abc)
        angles = np.array(crystal.lattice.angles)
        # not currently used.
        label = (label + 1.7021)
        # also not currently used
        electronPadded = np.pad(electron, 5, 'symmetric')
        electron = electron.reshape((1, 30, 30, 30))
        electronPadded = electronPadded.reshape((1, 40, 40, 40))
        electron = torch.from_numpy(electron)
        electronPadded = torch.from_numpy(electronPadded)
        mat = torch.from_numpy(specie)
        label = torch.as_tensor([label])
        return (electronPadded.float(), electron.float(), label.float(),
                mat.float())

    def __len__(self):
        return len(self.input_data)


if __name__ == '__main__':
    dataset = CrystalDataset(0, 31)
    print(len(dataset))