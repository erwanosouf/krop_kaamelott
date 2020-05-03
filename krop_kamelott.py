#!/usr/bin/env python3

import sys
import os
import os.path
import ffmpeg


def mute(input, output):
    ffmpeg.input(input).output(output, **{ "af": "volume=enable='lt(t,3)':volume=0", "c:v" : "copy"}).overwrite_output().run()



sources = [ (item, os.path.splitext(item)[1]) for item in os.listdir(".") if os.path.isfile(item) and "kaamelott" in item.lower() ]

output_dir = "muted"
if not os.path.exists(output_dir) and sources:
    os.mkdir(output_dir)

for source in sources:
    mute(source[0], os.path.join(output_dir, source[0]))



