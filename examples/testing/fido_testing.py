from sunpy.net import Fido, attrs as a
import astropy.units as u

# Time range of data you are looking for
time = a.Time('2013/05/15 03:00',
              '2013/05/15 05:00')

# Instruments you want data from
aia = a.Instrument.aia                 # Instrument which produced the image
ste = a.Instrument.secchi

# Various Common wavelengths for intensity
wav_94 = a.Wavelength(94*u.angstrom)      # AIA
wav_131 = a.Wavelength(131*u.angstrom)      # AIA
wav_171 = a.Wavelength(171*u.angstrom)      # Stereo | AIA
wav_193 = a.Wavelength(193*u.angstrom)      # AIA
wav_195 = a.Wavelength(195*u.angstrom)      # Stereo | AIA (193)
wav_284 = a.Wavelength(284*u.angstrom)      # Stereo
wav_304 = a.Wavelength(304*u.angstrom)      # Stereo | AIA
wav_335 = a.Wavelength(335*u.angstrom)      # AIA

#
cad = a.Sample(1*u.minute)              # Cadence (one image every [timeframe])
phy = a.Physobs('Intensity')            # Physical Observable (What quantity?)
ext = a.ExtentType('FULLDISK')          # Extent of the observation (how much of the sun)

# Include all of your properties in the Fido.search call
result = Fido.search(time, ste, cad, phy, wav_195)
table = result.show('Start Time', 'End Time', 'Source')

print(table)

# Select your recorded event from the results list ([0, #number of the row you want])
sel = result[0, 0]
print(sel)
#
# # Put more than one selection in this list if you want
# sels = [sel]
#
# # Download each of the search items you have selected
# for sel in sels:
#     download = Fido.fetch(sel, path='./downloaded_events/2013-05-15')    # Downloads the selected event found via Fido.search to
#                                                               # the specified path
#     print(download.errors)                                    # Output any errors that might have prevented download
