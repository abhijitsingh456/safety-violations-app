Vue.createApp({
    data() {
        return {
            isSidebarCollapsed: false,
            selectedFile: null,
            uploadedFilesHistory: []
        };
    },
    methods: {
        toggleSidebar() {
            this.isSidebarCollapsed = !this.isSidebarCollapsed;
        },
        handleFileUpload(event) {
            this.selectedFile = event.target.files[0];
        },
        async submitFile() {
            if (!this.selectedFile) return;

            const formData = new FormData();
            formData.append('file', this.selectedFile);

            try {
                const response = await fetch('/api/upload_from_old_camera', {
                    method: 'POST',
                    body: formData
                });

                if (response.ok) {
                    this.selectedFile = null;
                    document.getElementById('fileUpload').value = '';
                    alert('File uploaded successfully!');
                } else {
                    alert('Upload failed.');
                }
            } catch (error) {
                console.error(error);
                alert('Error uploading file.');
            }
        },
        async getUplodHistory(){
            url='/api/history_upload_from_old_camera'
            try{
                const response = await fetch(url)
                if (!response.ok){
                    throw new Error(`Respose Status: ${response.status}`)
                }
                this.uploadedFilesHistory = await response.json();
            }catch(error){
                console.error(error.message)
            }            
        }
    },
    mounted() {
        this.getUplodHistory()
      },
    delimiters: ['[[', ']]'],
}).mount('#app');