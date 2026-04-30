"""Generate per-segment narration using edge-tts (US English neural voice)."""
import asyncio
import json
import edge_tts
from mutagen.mp3 import MP3

# en-US-GuyNeural = neutral male US voice (Silicon Valley style)
VOICE = "en-US-GuyNeural"
RATE = "+0%"  # natural pace

SEGMENTS = [
    {"id": "intro", "text": "Introducing eHardware. Custom hardware designs and products for embedded systems."},
    {"id": "f1", "text": "Feature one. PCB Design Library. Production-ready schematics and layouts for common embedded platforms."},
    {"id": "f2", "text": "Feature two. FPGA Reference Designs. Synthesizable HDL for Xilinx and Lattice FPGAs with testbenches."},
    {"id": "f3", "text": "Feature three. Manufacturing Automation. Automated BOM generation, DRC checks, and Gerber export pipelines."},
    {"id": "arch", "text": "Under the hood, eHardware is built with KiCad, Verilog, and Python. The architecture flows from Schematic, to Layout, to DRC, to BOM Gen, to Gerber Export."},
    {"id": "cta", "text": "eHardware. Open source hardware for everyone. Visit github dot com slash embeddedos-org slash eHardware."}
]


async def generate():
    durations = {}
    audio_files = []

    for seg in SEGMENTS:
        filename = f"seg_{seg['id']}.mp3"
        communicate = edge_tts.Communicate(seg["text"], VOICE, rate=RATE)
        await communicate.save(filename)
        dur = MP3(filename).info.length
        durations[seg["id"]] = round(dur + 0.5, 1)
        audio_files.append(filename)
        print(f"  {seg['id']}: {dur:.1f}s -> padded {durations[seg['id']]}s")

    with open("durations.json", "w") as f:
        json.dump(durations, f, indent=2)

    # Concatenate
    import subprocess
    with open("concat_list.txt", "w") as f:
        for af in audio_files:
            f.write(f"file '{af}'\n")

    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", "concat_list.txt", "-c", "copy", "narration.mp3"
    ], check=True)

    total = sum(durations.values())
    print(f"\nVoice: {VOICE}")
    print(f"Total narration: {total:.1f}s")
    print(f"Durations: {json.dumps(durations)}")


asyncio.run(generate())
