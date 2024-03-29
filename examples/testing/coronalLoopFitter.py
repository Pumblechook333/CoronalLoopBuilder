from CoronalLoopBuilder.builder import CoronalLoopBuilder
import pickle
import matplotlib.pyplot as plt
import astropy.units as u

year = 2012
wav = 171
stereo = 'A'

maps = []
mapdirs = [f'maps/{year}/AIA-{str(wav)}.pkl', f'maps/{year}/STEREO{stereo}-{str(wav)}.pkl']

for name in mapdirs:
    with open(name, 'rb') as f:
        maps.append(pickle.load(f))
        f.close()

num_maps = len(maps)

# Visualize the dummy maps
fig = plt.figure(figsize=(6 * num_maps, 6))
axs = []
for midx, dummy_map in enumerate(maps):
    ax = fig.add_subplot(1, num_maps, midx + 1, projection=dummy_map)
    axs.append(ax)
    dummy_map.plot(alpha=0.75, axes=ax)
    dummy_map.draw_grid(axes=ax, grid_spacing=10 * u.deg, color='k')
    dummy_map.draw_limb(axes=ax, color='k')
    ax.set_title(ax.get_title(), pad=45)

coronal_loop1 = CoronalLoopBuilder(fig, axs, maps, pkl=f'loop_params/{year}/front_{year}.pkl', color='red')
coronal_loop2 = CoronalLoopBuilder(fig, axs, maps, pkl=f'loop_params/{year}/back_{year}.pkl', color='blue')
# coronal_loop1 = CoronalLoopBuilder(fig, axs, maps, pkl=f'loop_params/{year}/front_{year}_slant.pkl', color='red')
# coronal_loop2 = CoronalLoopBuilder(fig, axs, maps, pkl=f'loop_params/{year}/back_{year}_slant.pkl', color='blue')

# fname = f'clb_{str(wav)}_{year}_adj'
# fig.savefig('figs/' + fname + '.jpg', dpi=300, bbox_inches='tight')

plt.show()
plt.close()
#
# coronal_loop1.save_params_to_pickle(f"{year}/front_{year}.pkl")
# coronal_loop2.save_params_to_pickle(f"{year}/back_{year}.pkl")

