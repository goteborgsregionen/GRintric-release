from instorage.files.audio import AudioMimeTypes
from instorage.files.image import ImageMimeTypes
from instorage.files.text import TextMimeTypes

MIMETYPE_EXTENSIONS_MAPPER = {
    # TEXT
    TextMimeTypes.MD.value: [".md", ".markdown", ".mdown", ".markdn"],
    TextMimeTypes.TXT.value: [".txt", ".text"],
    TextMimeTypes.PDF.value: [".pdf"],
    TextMimeTypes.DOCX.value: [".docx"],
    TextMimeTypes.TEXT_CSV.value: [".csv"],
    TextMimeTypes.APP_CSV.value: [".csv"],
    TextMimeTypes.PPTX.value: [".pptx"],
    # AUDIO
    AudioMimeTypes.M4A.value: [".m4a"],
    AudioMimeTypes.OGG.value: [".oga", ".ogg", ".spx", ".opus"],
    AudioMimeTypes.WAV.value: [".wav"],
    AudioMimeTypes.MPEG.value: [".mp3", ".mp2", ".mpga", ".mp2a", ".m2a", ".m3a"],
    AudioMimeTypes.MP3.value: [".mp3"],
    # IMAGE
    ImageMimeTypes.PNG.value: [".png"],
    ImageMimeTypes.JPEG.value: [".jpeg", ".jpg", ".jpe"],
}