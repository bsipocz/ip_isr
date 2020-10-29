# This file is part of ip_isr.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# import os

import lsst.pex.config as pexConfig
import lsst.pipe.base as pipeBase
from lsst.meas.algorithms import (SubtractBackgroundTask, SourceDetectionTask)


class AmpOffsetConfig(pexConfig.Config):
    """Configuration parameters for AmpOffsetTask.
    """
    ampEdgeInset = pexConfig.Field(
        doc="Number of pixels the amp edge strip is inset from the amp edge. A thin strip of pixels running "
        "parallel to the edge of the amp is used to characterize the average flux level at the amp edge.",
        dtype=int,
        default=5,
    )
    ampEdgeWidth = pexConfig.Field(
        doc="Pixel width of the amp edge strip, starting at ampEdgeInset and extending inwards.",
        dtype=int,
        default=64,
    )
    ampEdgeMinFrac = pexConfig.Field(
        doc="Minimum allowed fraction of viable pixel rows along an amp edge. No amp-to-amp step estimate "
        "will be generated for amp edges that do not have at least this fraction of unmasked pixel rows.",
        dtype=float,
        default=0.5,
    )
    ampEdgeMaxStep = pexConfig.Field(
        doc="Maximum allowed amp-to-amp step value. If a measured amp-to-amp step value is larger than this, "
        "the result will be discarded and therefore not used to determine amp offset piston corrections.",
        dtype=float,
        default=5.0,
    )
    ampEdgeWindow = pexConfig.Field(
        doc="Size of the sliding window used to generate rolling average amp-edge step values.",
        dtype=int,
        default=512,
    )
    background = pexConfig.ConfigurableField(
        doc="An initial background estimation step run prior to amp offset calculation.",
        target=SubtractBackgroundTask,
    )
    detection = pexConfig.ConfigurableField(
        doc="Source detection to add temporary detection footprints prior to amp offset calculation.",
        target=SourceDetectionTask,
    )


class AmpOffsetTask(pipeBase.Task):
    """Calculate and apply amp offset corrections to an exposure.
    """
    ConfigClass = AmpOffsetConfig
    _DefaultName = "isrAmpOffset"

    def run(self, exposure):
        """Calculate amp-to-amp step values, determine corrective piston
        pedestals for each amp, and update the input exposure in-place. This
        task is currently not implemented, and should be retargeted by a camera
        specific version.

        Parameters
        ----------
        exposure : `lsst.afw.image.Exposure`
            Exposure to be corrected for any amp-to-amp offsets.
        """
        raise NotImplementedError("Amp offset task should be retargeted by a camera specific version.")
