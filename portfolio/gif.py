
from moviepy.editor import *
def time_symetrize(clip):
    return concatenate([clip, clip.fx( vfx.time_mirror )])
clip = (VideoFileClip("vivi.mp4")
        .subclip((0,3),(0,7))
        .resize(0.8)
        .fx( time_symetrize ))
clip.write_gif("rand.gif")

#http://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/
#https://docs.aws.amazon.com/lambda/latest/dg/python-package.html
#10 sec ~ 15MB ( without optimization)
#background removal is also possible, but works well when the 
#background is static in nature.
#watermark the gif , important it seems. coz novel solution.
#https://github.com/Zulko/moviepy/issues/885

'''
#optimize the gif using gifsicle
from pygifsicle import optimize
optimize("river_out2.gif")
'''