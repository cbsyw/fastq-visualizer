import { useState, useRef } from 'react'


function FileUpload({ onUpload }) {

    const [selectedFile, setSelectedFile] = useState(null)
    const fileInputRef = useRef(null)

    function handleFileSelect(event) {
        const file = event.target.files[0]
        setSelectedFile(file)
    }
    
    async function handleUpload() {
        if (!selectedFile) return

        await onUpload(selectedFile)

        setSelectedFile(null)

        fileInputRef.current.value = ''
    }



return (
    <div>
        <input 
        id="file-input" 
        type="file" 
        accept=".fastq,.fq" 
        onChange={handleFileSelect}
        style={{ display: 'none'}}
        />
        <label htmlFor="file-input" className='upload-button'>
            Choose FastQ file
        </label>
         {selectedFile && (
        <p>{selectedFile.name} ({(selectedFile.size/1000).toFixed(1)} KB)</p>
        )}
        <button 
            onClick={handleUpload}
            disabled={!selectedFile}
        >
            Analyze FASTQ
        </button>
    </div>
    )
}

export default FileUpload
