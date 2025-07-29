


# import flet as ft
# import os
# from yt_dlp import YoutubeDL

# def main(page: ft.Page):
#     page.title = "YouTube Downloader"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.bgcolor = ft.Colors.BLUE_GREY_100

#     titulo = ft.Text("YouTube Downloader", size=40, weight=ft.FontWeight.BOLD)
#     titulo.color = ft.Colors.BLACK
#     titulo.alignment = ft.alignment.center
#     titulo.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     titulo.padding = 20

#     url_input = ft.TextField(label="YouTube URL", width=400)
#     save_path = ft.Text("Chosen directory: Not selected yet")
#     status_text = ft.Text("")
#     progress_bar = ft.ProgressBar(width=400, visible=False)


#     def on_dialog_result(e: ft.FilePickerResultEvent):
#         if e.path:
#             save_path.value = f"Chosen directory: {e.path}"
#         else:
#             save_path.value = "Chosen directory: Not selected yet"
#         save_path.update()

#     file_picker = ft.FilePicker(on_result=on_dialog_result)
#     page.overlay.append(file_picker)

#     def baixar(formato):
#         if not url_input.value or not file_picker.result or not file_picker.result.path:
#             status_text.value = "Please provide a URL and a directory."
#             status_text.update()
#             return

#         url = url_input.value.strip()
#         caminho = file_picker.result.path

#         try:
#             status_text.value = f"Downloading {formato}..."
#             progress_bar.visible = True
#             page.update()
#             status_text.update()
#             page.update()

#             if formato == "video":
#                 ydl_opts = {
#                     'format': 'best[ext=mp4]/best',
#                     'outtmpl': os.path.join(caminho, '%(title)s.%(ext)s'),
#                     'merge_output_format': 'mp4',  # só usado se FFmpeg estiver presente
#                 }
#             else:
#                 ydl_opts = {
#                     'format': 'bestaudio[ext=m4a]/bestaudio',
#                     'outtmpl': os.path.join(caminho, '%(title)s.%(ext)s'),
#                     'postprocessors': [],  # Não converte para mp3 (sem FFmpeg)
#                 }

#             with YoutubeDL(ydl_opts) as ydl:
#                 ydl.download([url])

#             status_text.value = "Download complete!"
#             progress_bar.visible = False
#             page.update()
#             status_text.update()
#         except Exception as ex:
#             status_text.value = f"Error: {ex}"
#             status_text.update()

#     page.add(
#         ft.Column(
#             [
#                 titulo,
#                 url_input,
#                 ft.Row(
#                     [
#                         ft.ElevatedButton("Choose Directory", on_click=lambda _: file_picker.get_directory_path()),
#                         ft.ElevatedButton("Download Video", on_click=lambda _: baixar("video")),
#                         ft.ElevatedButton("Download Audio", on_click=lambda _: baixar("audio")),
                        
#                     ],
#                     alignment=ft.MainAxisAlignment.CENTER,
#                 ),
#                 save_path,
#                 status_text,
#                 progress_bar,
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#         )
#     )

# if __name__ == "__main__":
#     ft.app(target=main)






import flet as ft
import os
from yt_dlp import YoutubeDL

def main(page: ft.Page):
    page.title = "YouTube Downloader"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLUE_GREY_100

    titulo = ft.Text("YouTube Downloader", size=40, weight=ft.FontWeight.BOLD)
    titulo.color = ft.Colors.BLACK
    titulo.alignment = ft.alignment.center
    titulo.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    titulo.padding = 20

    url_input = ft.TextField(label="YouTube URL", width=400)
    save_path = ft.Text("Chosen directory: Not selected yet")
    status_text = ft.Text("")
    progress_bar = ft.ProgressBar(width=400, visible=False)

    def get_id_video(url):
        # Extrai o ID do vídeo da URL
        if "youtube.com/watch?v=" in url:
            print(url.split("v=")[-1].split("&")[0])
            return url.split("v=")[-1].split("&")[0]
        else:
            return None

    def on_dialog_result(e: ft.FilePickerResultEvent):
        if e.path:
            save_path.value = f"Chosen directory: {e.path}"
        else:
            save_path.value = "Chosen directory: Not selected yet"
        save_path.update()

    file_picker = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)

    def baixar_legenda(video_id):
        from youtube_transcript_api import YouTubeTranscriptApi
        from youtube_transcript_api.formatters import SRTFormatter

        try:
            # Obter a lista de transcrições disponíveis
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

            # Encontrar a transcrição em inglês
            transcript = transcript_list.find_transcript(['en'])

            # Traduzir para português
            translated_transcript = transcript.translate('pt')

            # Obter o texto traduzido
            translated_text = translated_transcript.fetch()

            # Cria o objeto SRTFormatter
            formatter = SRTFormatter()

            # Format the transcript to SRT
            srt_formatted = formatter.format_transcript(translated_text)

            # Now we can write it out to a file.
            with open(f'{titulo}.srt', 'w', encoding='utf-8') as json_file:
                json_file.write(srt_formatted)


        except Exception as ex:
                status_text.value = f"Não achou nenhuma legenda para baixar: baixando somente o video ou o audio"
                status_text.update()
                return


    def baixar(formato):
        if not url_input.value or not file_picker.result or not file_picker.result.path:
            status_text.value = "Please provide a URL and a directory."
            status_text.update()
            return

        url_id = get_id_video(url_input.value.strip())
        url = url_input.value.strip()
        caminho = file_picker.result.path

        try:
            status_text.value = f"Downloading {formato}..."
            progress_bar.visible = True
            page.update()
            status_text.update()
            page.update()

            if formato == "video":
                ydl_opts = {
                    'format': 'best[ext=mp4][height<=720][acodec!=none][vcodec!=none]/best',
                    'outtmpl': os.path.join(caminho, '%(title)s.%(ext)s'),
                    'merge_output_format': 'mp4',  # só usado se FFmpeg estiver presente
                }
            else:
                ydl_opts = {
                    'format': 'bestaudio[ext=m4a]/bestaudio',
                    'outtmpl': os.path.join(caminho, '%(title)s.%(ext)s'),
                    'postprocessors': [],  # Não converte para mp3 (sem FFmpeg)
                }

            baixar_legenda(url_id)

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            status_text.value = "Download complete!"
            progress_bar.visible = False
            page.update()
            status_text.update()
        except Exception as ex:
            status_text.value = f"Error: {ex}"
            status_text.update()

    page.add(
        ft.Column(
            [
                titulo,
                url_input,
                ft.Row(
                    [
                        ft.ElevatedButton("Choose Directory", on_click=lambda _: file_picker.get_directory_path()),
                        ft.ElevatedButton("Download Video", on_click=lambda _: baixar("video")),
                        ft.ElevatedButton("Download Audio", on_click=lambda _: baixar("audio")),
                        
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                save_path,
                status_text,
                progress_bar,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)