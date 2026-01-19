from Bio import SeqIO

# for record in SeqIO.parse(filepath, "fastq"):
#     print(record.id)
#     print(record.seq)
#     print(record.letter_annotations["phred_quality"])

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

    try:
        for record in SeqIO.parse(filepath, "fastq"):
            total_sequences += 1
            all_gc_values.append(calculate_gc_content(record.seq))
            all_quality_scores.extend(record.letter_annotations["phred_quality"])
            sequence_lengths.append(len(record.seq))
    except Exception as e:
        raise ValueError(f"Invalid FASTQ file: {str(e)}")

    avg_gc = sum(all_gc_values)/len(all_gc_values) 
    avg_quality = sum(all_quality_scores)/len(all_quality_scores)
    avg_length = sum(sequence_lengths)/len(sequence_lengths)

    
    fastq_analysis = {
        'total_sequences' : total_sequences,
        'avg_gc' : avg_gc,
        'avg_quality' : avg_quality,
        'avg_length' : avg_length
    }

    return fastq_analysis




if __name__ == "__main__":
    results = analyze_fastq("sample.fastq")
    print(f"Total sequences: {results['total_sequences']}")
    print(f"Avg GC%: {results['avg_gc']:.2%}")
    print(f"Avg quality: {results['avg_quality']:.1f}")
    print(f"Avg length: {results['avg_length']:.0f}")
   