import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import SkyCoord
import sunpy.map
from CoronalLoopBuilder.builder import CoronalLoopBuilder

map = sunpy.map.Map('./downloaded_events/aia_lev1_304a_2012_07_19t06_40_07_12z_image_lev1.fits')
map2 = sunpy.map.Map('./downloaded_events/20120719_063615_304_n4euA.fts')

tr = SkyCoord(1125*u.arcsec, -350*u.arcsec, frame=map.coordinate_frame)
bl = SkyCoord(850*u.arcsec, -150*u.arcsec, frame=map.coordinate_frame)
tr2 = SkyCoord(-300*u.arcsec, -450*u.arcsec, frame=map2.coordinate_frame)
bl2 = SkyCoord(-700*u.arcsec, -100*u.arcsec, frame=map2.coordinate_frame)

submap = map.submap(bl, top_right=tr)
submap2 = map2.submap(bl2, top_right=tr2)

maps = [submap, submap2]
# maps = [map, map2]

num_maps = len(maps)

# Visualize the dummy maps
fig = plt.figure(figsize=(6 * num_maps, 6))
axs = []
for midx, dummy_map in enumerate(maps):
    ax = fig.add_subplot(1, num_maps, midx + 1, projection=dummy_map)
    axs.append(ax)
    # dummy_map.plot(alpha=0.5, extent=[-1000, 1000, -1000, 1000], title=False, axes=ax)
    dummy_map.plot(alpha=0.75, axes=ax)
    dummy_map.draw_grid(axes=ax, grid_spacing=10 * u.deg, color='k')
    dummy_map.draw_limb(axes=ax, color='k')
    ax.set_title(ax.get_title(), pad=45)


# coronal_loop1 = CoronalLoopBuilder(fig, axs, maps, pkl='./loop_params/AIA_2011925.pkl')
# coronal_loop2 = CoronalLoopBuilder(fig, axs, maps, pkl='./loop_params/STEREOA_2011925.pkl')

coronal_loop1 = CoronalLoopBuilder(fig, axs, maps, radius = 28.0 * u.Mm,
                                   height = 15.0 * u.Mm, phi0 = 87.00 * u.deg,
                                   theta0 = -13.50 * u.deg, el = 90.00 * u.deg,
                                   az = -20.00 * u.deg, samples_num = 100)

coronal_loop2 = CoronalLoopBuilder(fig, axs, maps, radius = 28.0 * u.Mm, height = 15.0 * u.Mm,
                                   phi0 = 93.50 * u.deg, theta0 = -15.00 * u.deg,
                                   el = 90.00 * u.deg, az = -20.00 * u.deg, samples_num = 100)

plt.show()
plt.close()
#
# coronal_loop2.save_map_to_pickle("AIA-STEREOA_304_2012.pkl")


