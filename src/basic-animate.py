# Adapted from GetoCAT > Getting Started > [Basic
# Examples](https://geocat-comp.readthedocs.io/en/stable/getting_started/mini-examples.html)
# and [NCL animate
# example](https://geocat-examples.readthedocs.io/en/latest/gallery/Animations/NCL_animate_1.html#sphx-glr-gallery-animations-ncl-animate-1-py)
#

import cartopy.crs as ccrs
import datetime
import geocat.viz as gv
import matplotlib.animation as animation
import numpy as np
import xarray as xr
from geocat.comp import calendar_average
from matplotlib import pyplot as plt


def main():
    # open NetCDF file using xarray
    ds = xr.open_dataset("/var/data/ncar-rda/d084006/T170/20070821_T170_1.nc")
    # ds.info()  # dump info to stdout
    temps = ds.TS  # get surface temperature
    # print(temps.coords["time"])

    # Convert temps from K to F
    temps.values = [
        (temps.values[i] - 273.15) * 9 / 5 + 32 for i in range(len(temps.values))
    ]

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
        vmin=-110,
        vmax=130,
        levels=53,
        cmap="inferno",
        add_colorbar=False,
    )

    # Create a colorbar
    cbar = fig.colorbar(
        cplot,
        extendrect=True,
        orientation="horizontal",
        ticks=np.arange(-110, 130, 20),
        label="",
        shrink=0.90,
    )

    # Remove minor ticks from colorbar that don't work well with other
    # formatting
    cbar.ax.minorticks_off()

    # Animate function for matplotlib FuncAnimation
    def animate(i):
        temps[i, :, :].plot.contourf(
            ax=ax,
            transform=ccrs.PlateCarree(),
            vmin=-110,
            vmax=130,
            levels=53,
            cmap="inferno",
            add_colorbar=False,
        )

        gv.set_titles_and_labels(
            ax,
            maintitle="Global Surface Temperature (F)\n"
            + str(ds.date.values[i])
            + " "
            + str(datetime.timedelta(seconds=int(ds.datesec.values[i]))),
            xlabel="",
            ylabel="",
        )

    # Run the animation initiated with the frame from init and progressed with the animate function
    anim = animation.FuncAnimation(fig, animate, frames=30, interval=0)

    anim.save("animate_1.gif", writer="pillow", fps=5)


if __name__ == "__main__":
    main()
