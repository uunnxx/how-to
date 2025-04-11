# import shlex, subprocess
#
# file = 'file name ~$~%$$&``'

# command_line = f'ffmpeg -stream_loop -1 -i "./temp/{file}.mp4" -c copy -v 0 -f nut - | ffmpeg -thread_queue_size 100M -i - -i "./temp/{file}.mp3" -c copy -map 0:v -map 1:a -shortest -y "./output/{file}.mp4"'

# print(shlex.split(command_line))
