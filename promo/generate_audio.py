"""Generate narration audio using Google Text-to-Speech."""
from gtts import gTTS

NARRATION = (
    "Introducing eHardware. Custom hardware designs and products for embedded systems. Feature one: A comprehensive PCB design library with production-ready schematics. Feature two: FPGA reference designs for rapid prototyping. Feature three: Manufacturing automation pipelines from design to production. eHardware. Open source hardware for everyone. Visit github dot com slash embeddedos-org slash eHardware."
)

tts = gTTS(text=NARRATION, lang="en", slow=False)
tts.save("narration.mp3")
print(f"Generated narration.mp3 ({len(NARRATION)} chars)")
