import astropy.units as u
import sunpy.map
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
import matplotlib.colors

map = sunpy.map.Map('./downloaded_events/aia_lev1_171a_2012_07_19t06_40_12_70z_image_lev1.fits')

top_right = SkyCoord(1125*u.arcsec, -350*u.arcsec, frame=map.coordinate_frame)   # 2011-09-25 STEREO A Frame
bottom_left = SkyCoord(850*u.arcsec, -150*u.arcsec, frame=map.coordinate_frame)

# submap = map.submap(bottom_left, top_right=top_right)
submap = map

fig = plt.figure()
ax = fig.add_subplot(projection=submap)
# image = submap.plot(axes=ax)
image = submap.plot(axes=ax, norm=matplotlib.colors.LogNorm())
submap.draw_limb(axes=ax)
submap.draw_grid(axes=ax)

ax.set_position([0.1, 0.1, 0.8, 0.7])
ax.set_title(ax.get_title(), pad=45)

fname = 'AIA171_fig_2012'

# fig.savefig('figs/pdfs/' + fname + '.pdf', dpi=300, bbox_inches='tight')
# fig.savefig('figs/' + fname + '.jpg', dpi=300, bbox_inches='tight')

plt.show()
