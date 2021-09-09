def run():
    from pytube import YouTube

    # callback function to show download progress
    def print_progress(stream, data_chunk, remaining_bytes):
        print(f"{remaining_bytes//1048576} MB remaining...")

    # callback function to notifiy downloading is finished
    def notify_download_finished(stream, file_path):
        print(
            f"\033[92mfinished downloading file on path: {file_path}\n -----------------------------------------------"
        )

    args = {"mime_type": "video/mp4", "res": "720p", "progressive": "True"}
    filename_prefix = "video-"

    while True:
        links = input(
            str(
                "paste here YouTube link/s you wish to download separated by a comma (or type 'exit' to leave): \n"
            )
        )
        if links.lower() == "exit":
            break
        audio_file_only = input(str("download audio file only? y/n "))
        try:
            links = [link.strip(" ") for link in links.split(",")]
            print(links)
            if audio_file_only.lower() == "y":
                args = {"abr": "128kbps", "mime_type": "audio/mp4"}
                filename_prefix = "audio-"
            for link in links:
                try:
                    yt = YouTube(link, print_progress, notify_download_finished)
                    print(
                        f"\033[93m{yt.title} file starting DOWNLOADING...\n -----------------------------------------------"
                    )
                    print("this might take few minutes...")
                    streams = yt.streams.filter(**args)
                    streams.first().download(filename_prefix=filename_prefix)
                except:
                    print(f"\033[91mlink {link} ---- FAILED!")
            print("\033[92m\033[1mALL DONE!")
            break
        except:
            print(f"at least one of the provided links is invalid, try again...")

run()
