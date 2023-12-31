```bash
ffmpeg -i input.mp4 -c:v libx264 -strftime 1 -strftime_mkdir 1 -hls_segment_filename %Y-%m-%d/v%H%M%S.ts -hls_time 30 -movflags faststart output.m3u8

ffmpeg -i input2.mp4 -c:v h264 -strftime 1 -strftime_mkdir 1 -hls_segment_filename %Y-%m-%d/v%H%M%S.ts -hls_time 30 -movflags faststart output.m3u8

ffmpeg -i free-video2-sea-cafinet.mp4 -c:v libx264 -b:v 800k -acodec libfaac -strftime 1 -strftime_mkdir 1 -hls_segment_filename %Y-%m-%d/v%H%M%S.ts -hls_time 30 -movflags faststart output.m3u8

ffmpeg -i input2.mp4 -f mp4 -vcodec libx264 -b:v 800k -acodec libfaac -b:a 128k -movflags faststart output.mp4

ffmpeg -i free-video2-sea-cafinet.mp4 -c:v libx264 -acodec libfaac -strftime 1 -strftime_mkdir 1 -hls_segment_filename %Y-%m-%d/v%H%M%S.ts -hls_time 5 -movflags faststart output.m3u8

ffmpeg -thread_queue_size 16384 -s 640x480 -vsync -1 -i "Integrated Camera" -c:v libx264 -b:v 1000k -bufsize 1000k -flags +cgop+loop-global_header -bsf:v h264_mp4toannexb -f segment -segment_format mpegts -segment_time 10 -segment_list stream.m3u8 segment%06d.ts

ffmpeg -input_format yuyv422 -video_size 352x288 -framerate 30 -i /dev/video0 -f hls -c:v libx264 -hls_time 1 -hls_list_size 10 -hls_flags delete_segments stream/out.m3u8


# 利用可能なカメラデバイスを確認する
ffmpeg -list_devices true -f dshow -i dummy

# 指定したカメラが利用できるふぉーっまとを確認する
ffmpeg -hide_banner -list_options true -f dshow -i video="Integrated Camera"

# カメラをinputとして動画ファイル作成
ffmpeg -f dshow -i video="Integrated Camera" video.mp4
ffmpeg -f dshow -i video="Integrated Camera" -loglevel debug output.mp4

# videoタグで再生可能なmp4にするコマンド
ffmpeg -i input2.mp4 -f mp4 -vcodec libx264 -acodec libfaac -b:a 128k -movflags faststart output.mp4

# videoタグで再生可能なm3u8にするコマンド
ffmpeg -i free-video2-sea-cafinet.mp4 -f hls -c:v libx264 -acodec libfaac -strftime_mkdir 1 -hls_time 5 -hls_segment_filename live%d.ts -movflags faststart output.m3u8


python frame2stdout.py | ffmpeg -r 30 -i - -c:v libx264 -strftime 1 -strftime_mkdir 1 -hls_segment_filename static/%Y-%m-%d/v%H%M%S.ts -sc_threshold 0 -g 30 -keyint_min $(awk "BEGIN { print 30 * 5 }") -hls_time 5 -loglevel debug zzz.m3u8


python frame2stdout.py | ffmpeg -r 30 -i - -c:v libx264 -strftime 1 -strftime_mkdir 1 -hls_segment_filename static/%Y-%m-%d/v%H%M%S.ts -sc_threshold 0 -hls_time 5 -loglevel debug zzz.m3u8

python frame2stdout.py | ffmpeg -r 30 -i - -c:v libx264 -strftime 1 -strftime_mkdir 1 -hls_segment_filename static/%Y-%m-%d/v%H%M%S.ts -sc_threshold 0 -hls_time 5 -loglevel debug static/zzz.m3u8

python ../frame2stdout.py | ffmpeg -r 30 -i - -f hls -c:v libx264 -acodec libfaac -strftime_mkdir 1 -hls_time 5 -hls_segment_filename live%d.ts -movflags faststart output.m3u8

# 完成
python ../frame2stdout.py | ffmpeg -r 30 -i - -f hls -c:v libx264 -acodec libfaac -strftime 1 -strftime_mkdir 1 -hls_time 5 -hls_segment_filename %Y-%m-%d/v%H%M%S.ts -movflags faststart output.m3u8

# 完成(C#版)
cs-camera-capture.exe | ffmpeg -r 30 -i - -f hls -c:v libx264 -acodec libfaac -strftime 1 -strftime_mkdir 1 -hls_time 15 -hls_segment_filename %Y-%m-%d/v%H%M%S.ts -movflags faststart output.m3u8

# v2
python ../frame2stdout.py | ffmpeg -r 30 -i - -f hls -c:v libx264 -acodec libfaac -strftime 1 -strftime_mkdir 1 -hls_time 5 -sc_threshold 0 -g 30 -keyint_min 150 -hls_segment_filename %Y-%m-%d/v%H%M%S.ts -movflags faststart output.m3u8

# v2(C#版)
cs-camera-capture.exe | ffmpeg -r 30 -i - -f hls -c:v libx264 -acodec libfaac -strftime 1 -strftime_mkdir 1 -hls_time 5 -sc_threshold 0 -g 30 -keyint_min 150 -hls_segment_filename %Y-%m-%d/v%H%M%S.ts -movflags faststart output.m3u8