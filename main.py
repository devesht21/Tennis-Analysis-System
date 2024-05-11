from utils import read_video, save_video
from constants import INPUT_VIDEO_PATH, OUTPUT_VIDEO_PATH


def main():
    # video_frames = read_video("inputs/input_video.mp4")
    video_frames = read_video(INPUT_VIDEO_PATH)

    # save_video(video_frames, "outputs/output_video.avi")
    save_video(video_frames, OUTPUT_VIDEO_PATH)


if __name__ == "__main__":
    main()
