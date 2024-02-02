from CoronalLoopBuilder.builder import CoronalLoopBuilder
import pickle
import matplotlib.pyplot as plt
import astropy.units as u
import sunpy

maps = []
mapdirs171 = ['maps/0_AIA-STEREOA_171_2012.pkl', 'maps/1_AIA-STEREOA_171_2012.pkl']
mapdirs195 = ['maps/0_AIA-STEREOA_195_2012.pkl', 'maps/1_AIA-STEREOA_195_2012.pkl']
mapdirs304 = ['maps/0_AIA-STEREOA_304_2012.pkl', 'maps/1_AIA-STEREOA_304_2012.pkl']
mapdirs304 = ['maps/1_AIA-STEREOA_304_2012.pkl']

for name in mapdirs304:
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

coronal_loop1 = CoronalLoopBuilder(fig, axs, maps, pkl='loop_params/back_2012.pkl', color='blue')
coronal_loop2 = CoronalLoopBuilder(fig, axs, maps, pkl='loop_params/front_2012.pkl', color='red', ellipse=True)

plt.show()
plt.close()

# coronal_loop1.save_params_to_pickle("back_2012.pkl")
# coronal_loop2.save_params_to_pickle("front_2012.pkl")
