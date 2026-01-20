
function Results({ data }) {

  if (!data) {
    return null  
  }
  
  const { total_sequences, avg_gc, avg_quality, avg_length } = data
  
  return (
    <div className="results">
      <h2>FASTQ Analysis Results</h2>
      
      <div className="metrics-grid">
        <div className="metric">
          <label>Total Sequences</label>
          <span>{total_sequences.toLocaleString()}</span>
        </div>
        
        <div className="metric">
          <label>Avg GC Content</label>
          <span>{(avg_gc * 100).toFixed(1)}%</span>
        </div>
        
        <div className="metric">
          <label>Avg Quality</label>
          <span>{avg_quality.toFixed(1)}</span>
        </div>
        
        <div className="metric">
          <label>Avg Length</label>
          <span>{Math.round(avg_length)}</span>
        </div>
      </div>
      
      <div className="interpretation">
        <p>Quality {avg_quality > 20 ? 'Good' : 'Low'}</p>
        <p>GC {avg_gc > 0.4 && avg_gc < 0.6 ? 'Normal' : 'Biased'}</p>
      </div>
    </div>
  )
}

export default Results