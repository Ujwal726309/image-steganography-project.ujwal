import os
import wave
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_file_path: str, wav_file_path: str) -> None:
    # Load the MP3 file using pydub
    audio = AudioSegment.from_mp3(mp3_file_path)
    
    # Export the audio to WAV format
    audio.export(wav_file_path, format='wav')
    

def em_audio(af, string, output):
    
    print ("Please wait...")
    waveaudio = wave.open(af, mode='rb')
    frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
    string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    frame_modified = bytes(frame_bytes)
    with wave.open(output, 'wb') as fd:
        fd.setparams(waveaudio.getparams())
        fd.writeframes(frame_modified)
    waveaudio.close()
    print ("Done...")


# Example usage:
mp3_file_path = 'temp_audio.mp3'
wav_file_path = 'def.wav'
convert_mp3_to_wav(mp3_file_path, wav_file_path)
em_audio(wav_file_path, "Hello My NAme is Shailesh.ihbdekfjgehdbisfujhe][[f[e[;v.rfkvmfjlduygfyyyyyyyyyyy]]]]", "output.wav")