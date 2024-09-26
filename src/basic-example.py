#
# Adapted from GetoCAT [Basic
# Examples](https://geocat-comp.readthedocs.io/en/stable/getting_started/mini-examples.html)
#

import cartopy.crs as ccrs
import geocat.viz as gv
import numpy as np
import xarray as xr
from matplotlib import pyplot as plt


def main():
    # open NetCDF file using xarray
    ds = xr.open_dataset("/var/data/ncar-rda/d084006/T170/20070821_T170_1.nc")
    # ds.info()  # dump info to stdout
    temps = ds.TS  # get surface temperature
    print(temps.shape)
    print(temps.coords["time"])

    fig = plt.figure(figsize=(10, 8))

    # Generate axes using Cartopy and draw coastlines
    ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=150))
    ax.coastlines(linewidths=0.5)
    ax.set_extent([-180, 180, -90, 90], ccrs.PlateCarree())

    # Use geocat-viz to set axes limits & tick values
    gv.set_axes_limits_and_ticks(
        ax,
        xlim=(-180, 180),
        ylim=(-90, 90),
        xticks=np.linspace(-180, 180, 13),
        yticks=np.linspace(-90, 90, 7),
    )

    # Use geocat-viz to add minor and major tick lines
    gv.add_major_minor_ticks(ax, labelsize=10)

    # Use geocat-viz to make latitude, longitude tick labels
    gv.add_lat_lon_ticklabels(ax)

    # Create initial plot
    cplot = temps[0, :, :].plot.contourf(
        ax=ax,
        transform=ccrs.PlateCarree(),
        vmin=195,
        vmax=328,
        levels=53,
        cmap="inferno",
        add_colorbar=False,
    )

    # Create a colorbar
    cbar = fig.colorbar(
        cplot,
        extendrect=True,
        orientation="horizontal",
        ticks=np.arange(195, 332, 9),
        label="",
        shrink=0.90,
    )

    # Remove minor ticks from colorbar that don't work well with other
    # formatting
    cbar.ax.minorticks_off()

    gv.set_titles_and_labels(
        ax,
        maintitle="January Global Surface Temperature (K) - Day  "
        + str(temps.coords["time"].values[i])[:13],
        xlabel="",
        ylabel="",
    )

    plt.show(block=True)


if __name__ == "__main__":
    main()
