
from Bio import SeqIO

for record in SeqIO.parse("file.fastq", "fastq"):
    print(record.id)
    print(record.seq)
    print(record.letter_annotation["phred_quality"])

def calculate_gc_content(sequence):

    total_gc = 0
    total_s = len(sequence)
    for letter in sequence:
        if letter == 'G' or letter == 'C':
            total_gc += 1
    gc_content = total_gc/total_s  

    return gc_content
        

def calculate_avg_quality(quality_scores):

    total_quality = sum(quality_scores)
    total_possible = len(quality_scores) 
    avg_quality = total_quality/total_possible

    return avg_quality


def analyze_fastq(filepath):

    total_sequences = 0
    all_gc_values = []
    all_quality_scores = []
    sequence_lengths = []

    pass


if __name__ == "__main__":
    results = analyze_fastq("sample.fastq")
    print(results)