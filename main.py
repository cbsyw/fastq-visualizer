
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from Bio import SeqIO
import tempfile
import os
from parse_fastq import analyze_fastq


app = FastAPI()


@app.post("/upload")
async def upload_fastq(file: UploadFile = File(...)):

    if not file.filename.endswith(('.fastq', '.fq')):
        return {"error": "File must be .fastq or .fq format"}

    print(f"Received file: {file.filename}")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".fastq") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    print(f"Temp file created at: {tmp_path}")

    results = analyze_fastq(tmp_path)

       
    print(f"Results: {results}") 

    os.unlink(tmp_path)

    return results