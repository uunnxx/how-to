# %w -- array without string interpolation
# %W -- array with string interpolation
# -----------------------------------------------------------------------------

# system "ln -s file1 file2"
# system 'ln', '-s', 'file1', 'file2'


command = 'ln'
options = '-s'
arguments = 'file1 file2'

# system command + options + arguments # no spaces between arguments
# i.e: ln-sfile1 file2

# we could use arrays

command1 = ['ln']
options1 = ['-s']
arguments1 = ['file1 file2']

# system *(command1 + options1 + arguments1)
puts *(command1 + options1 + arguments1)

# -----------------------------------------------------------------------------

%w[file1 file2]

recording_options = %w[-f x11grab -s 960x600 -i 0:0+800,300 -r 30]
misc_optionss = %w[-sameq -threads 6]
output_options = %w[screencast.mp4]

ffmpeg_flags =
  recording_options +
  misc_optionss +
  output_options

# system 'ffmpeg', *ffmpeg_flags

# -----------------------------------------------------------------------------
width = 960
height = 600

recording_options = %W[-f x11grab -s #{width}x#{height} -i 0:0+800,300 -r 30]
misc_optionss = %w[-sameq -threads 6]
output_options = %w[screencast.mp4]

ffmpeg_flags =
  recording_options +
  misc_optionss +
  output_options

# system 'ffmpeg', *ffmpeg_flags
