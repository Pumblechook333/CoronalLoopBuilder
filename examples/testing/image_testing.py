import astropy.units as u
import sunpy.map
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
import matplotlib.colors
import os
import pickle

map = sunpy.map.Map('./downloaded_events/2013-05-15/aia_lev1_304a_2013_05_15t04_14_07_12z_image_lev1.fits')

top_right = SkyCoord(-750*u.arcsec, 300*u.arcsec, frame=map.coordinate_frame)   # 2011-09-25 STEREO A Frame
bottom_left = SkyCoord(-950*u.arcsec, 100*u.arcsec, frame=map.coordinate_frame)

submap = map.submap(bottom_left, top_right=top_right)
# submap = map

fig = plt.figure()
ax = fig.add_subplot(projection=submap)
image = submap.plot(axes=ax)
# image = submap.plot(axes=ax, norm=matplotlib.colors.LogNorm())
submap.draw_limb(axes=ax)
submap.draw_grid(axes=ax)

ax.set_position([0.1, 0.1, 0.8, 0.7])
ax.set_title(ax.get_title(), pad=45)

# fname = 'STB195_fig_2013'

# fig.savefig('figs/pdfs/' + fname + '.pdf', dpi=300, bbox_inches='tight')
# fig.savefig('figs/' + fname + '.jpg', dpi=300, bbox_inches='tight')

plt.show()
plt.close()

filename = 'AIA-304.pkl'
dirname = 'maps/2013'

os.makedirs(f'./{dirname}', exist_ok=True)

with open(f'./{dirname}/{filename}', 'wb') as file:
    pickle.dump(submap, file)
    file.close()
print(f"Map saved to './{dirname}/{filename}'!")