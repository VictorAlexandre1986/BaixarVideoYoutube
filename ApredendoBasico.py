from youtube_transcript_api import YouTubeTranscriptApi

def basico():
    video_id="8pn9KEuXG28"
    transcricao = YouTubeTranscriptApi()
    transcrito = transcricao.fetch(video_id=video_id, languages=["pt","en"])

    lista_transcrito = list()

    for trecho in transcrito:
        print(f"text={trecho.text}  ")
        print(f"start={trecho.start}")
        print(f"duration={trecho.duration}")

        lista_transcrito.append(trecho)
        # print(lista_transcrito)

    last_snippet = lista_transcrito[-1]
    print(f"Ultimo trecho: {last_snippet.text} - Início: {last_snippet.start} - Duração: {last_snippet.duration}")



    #Transcrição crua
    transcricao_crua = transcrito.to_raw_data()
    # print(transcricao_crua)

def basico2():
    video_id = "8pn9KEuXG28"  # Substitua pelo ID do vídeo desejado
    lista_transcricoes_disponiveis = YouTubeTranscriptApi()
    lista_transcrito1 = lista_transcricoes_disponiveis.list(video_id=video_id)
    print(lista_transcrito1)



def transcricoes_disponiveis():

    #Por padrão, este módulo sempre escolhe transcrições criadas manualmente sobre as
    # criadas automaticamente, se uma transcrição no idioma solicitado estiver disponível,
    # criado manualmente e gerado manualmente. O TranscriptList permite ignorar esse
    # comportamento padrão pesquisando tipos de transcrição específicos:



    lista_transcricoes_disponiveis2 = YouTubeTranscriptApi()
    try:
        # Get list of all available transcripts
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Try to find manual transcript
        try:
            transcript = transcript_list.find_manually_created_transcript(['pt', 'en'])
            print("Manual transcript found:")
            print(transcript.fetch())
            print(transcript.language_code)
            print(transcript.language_name)
            print(transcript.is_generated)
            print(transcript.is_translatable)
        except:
            print("No manual transcript found in specified languages")

        # Try to find generated transcript
        try:
            transcript = transcript_list.find_generated_transcript(['pt', 'en'])
            print("Generated transcript found:")
            print(transcript.fetch())
            print(transcript.language_code)
            print(transcript.language_name)
            print(transcript.is_generated)
            print(transcript.is_translatable)
        except:
            print("No generated transcript found in specified languages")

    except Exception as e:
        print(f"Error: {e}")
        print("Could not retrieve transcript list for this video")

def tradutor():
    from youtube_transcript_api import YouTubeTranscriptApi

    video_id = "8pn9KEuXG28"

    try:
        # Obter a lista de transcrições disponíveis
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Encontrar a transcrição em inglês
        transcript = transcript_list.find_transcript(['en'])

        # Traduzir para português
        translated_transcript = transcript.translate('pt')

        # Obter o texto traduzido
        translated_text = translated_transcript.fetch()

        print(translated_text)

        # Imprimir a transcrição traduzida
        for entry in translated_text:
            print(f"{entry['start']:.2f} - {entry['text']}")

    except Exception as e:
        print(f"Erro: {e}")
        print("Verifique se o vídeo possui legendas em inglês disponíveis.")





from googletrans import Translator # Estudar depois
from youtube_transcript_api import YouTubeTranscriptApi
from translate import Translator


def tradutor_google():
    video_id = "8pn9KEuXG28"  # Substitua pelo ID do vídeo desejado

    try:
        # Obter a transcrição do vídeo (em inglês ou português)
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'pt'])

        # Inicializar o tradutor (configuração correta para Português)
        translator = Translator(from_lang='en', to_lang='pt')

        # Traduzir cada entrada da transcrição (se estiver em inglês)
        for entry in transcript:
            texto = entry['text']

            # Tentar traduzir (assumindo que o texto está em inglês)
            try:
                traducao = translator.translate(texto)
                print(f"{entry['start']:.2f}s - Original: {texto}")
                print(f"Tradução (pt): {traducao}\n")
            except Exception as trad_error:
                print(f"{entry['start']:.2f}s - Erro na tradução ou texto já em PT: {texto}\n")

    except Exception as e:
        print(f"Erro: {e}")
        print("Verifique se o vídeo possui legendas disponíveis.")


# Chamar a função
# tradutor_google()

if __name__ == "__main__":
    tradutor_google()