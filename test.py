import numpy as np
from Generate import get_structure, read_in_properties, generate
import pickle
import tqdm

s_dir = '/home/luoxs/data_preperation/crys_hoffmann/'
target = read_in_properties('/home/luoxs/data_preperation/id_prop.csv')
to_save = []
#for i in tqdm.tqdm(range(0, 10)):
#    crystal = get_structure(s_dir + str(i) + '.cif')
#    abc = np.array(crystal.lattice.abc)
#    if min(abc) < 10:
#        electron_density, electron_density2 = generate(crystal, 0, 0, 0)
#        to_save.append([i, electron_density, electron_density2, target[i]])
#        electron_density, electron_density2 = generate(crystal,
#                                                       10 * np.random.rand(),
#                                                       10 * np.random.rand(),
#                                                       10 * np.random.rand())
#        to_save.append([i, electron_density, electron_density2, target[i]])
#        electron_density, electron_density2 = generate(crystal,
#                                                       10 * np.random.rand(),
#                                                       10 * np.random.rand(),
#                                                       10 * np.random.rand())
#        to_save.append([i, electron_density, electron_density2, target[i]])
#
#with open('/home/luoxs/data_preperation/SAVE/S_3x_' + '1' + '.pickle', 'wb') as f:
#    pickle.dump(to_save, f)

data = np.vstack([pickle.load(open('/home/luoxs/data_preperation/SAVE/S_3x_'+str(i)+'.pickle', 'rb'), encoding='bytes') for i in range(1, 2)])
print(data.shape)
print(max(data[0, 1].shape))